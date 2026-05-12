# AGENTS.md — nexia-soluciones Landing Page
> Estado del proyecto. Actualizar al cerrar cada tarea.
> Última actualización: 2026-05-12

## Estado actual
Landing page single-page con scroll continuo. Rutas dedicadas por app operativas (/planner, /facturacion, /tienda). Deploy via Hostinger GIT sincronizado con main. dist/ incluido en git (no en .gitignore) — requerido por el proceso de deploy de Hostinger.

## Deploy en Hostinger — Proceso definitivo ✅
1. Agente hace cambios en el código
2. `npm run build` (dist/ está incluido en git, NO en .gitignore)
3. `git push origin main`
4. Hostinger → GIT → Implementar
5. Avanzado → Administrador de caché → Borrar caché
6. Ctrl+F5 en navegador

## Rutas dedicadas por app (AppLanding.jsx)
- `nexiasoluciones.com.mx/planner` → NexIA Planner
- `nexiasoluciones.com.mx/facturacion` → Nexia Gastos
- `nexiasoluciones.com.mx/tienda` → Nexia Tienda
- Solo apps con `ctaActive: true` tienen ruta dedicada
- Para agregar nueva app: añadir objeto al array `products[]` en `AppLanding.jsx` + nueva `<Route>` en `App.jsx`
- Estas URLs se usan para campañas de venta por WhatsApp, Telegram, Facebook

## Completado ✅
- [x] Restauración del código desde Hostinger a ~/dev/nexia-soluciones
- [x] npm install + npm run dev funcionando
- [x] Repo conectado: github.com/HiramSpeed/nexia-soluciones
- [x] ParticleCanvas.jsx creado e integrado en App.jsx (partículas azul #00A3FF)
- [x] Header: CTA actualizado a "Agendar Auditoría Gratuita" en desktop y mobile
- [x] ProductsPage: rediseñado con 5 apps del ecosistema Lean (PDCA, Scholar, VSM, SMED, Heijunka)
- [x] ProductsPage: formulario de compra INLINE en card expandida con overlay oscuro (expandedCard state)
- [x] ProductsPage: Nexia Scholar como única app EN PRODUCCIÓN con ctaActive:true
- [x] Estándar de cards de apps documentado en CLAUDE.md
- [x] .env creado con VITE_N8N_VENTAS_WEBHOOK y VITE_N8N_CONTACTO_WEBHOOK
- [x] Scroll continuo single-page — ruta /productos eliminada
- [x] Sistema de tabs por grupos (Todos, Educación, Mejora Continua, Admin & Finanzas)
- [x] Tab "Todos" por defecto
- [x] Reset tab al navegar desde el menú
- [x] Card width limitado a 400px, grid centrado
- [x] Portafolio de Soluciones — encabezado rediseñado
- [x] Auto-reset card después de solicitud enviada (4 segundos → tab Todos)
- [x] Hero reemplazado por imagen hero-nexia.jpeg con botón CTA dorado superpuesto (bottom 3%, right 8%)
- [x] Migración ContactModal de Formspree a n8n nexia-contacto (ID: ZtFuhWdaP2mvjm75)
- [x] BCC en todos los correos: daniel.navarro@ y juan.garces@nexiasoluciones.com.mx
- [x] HTML profesional en correos de nexia-ventas con logo, slogan y datos bancarios
- [x] Flujos n8n verificados y activos: nexia-ventas + nexia-contacto

## Cambios n8n — 2026-05-06 ✅
- [x] nexia-ventas: datos bancarios reales — Banco Santander, CLABE 014215655116141623, Titular NEXIA SOLUCIONES SAS
- [x] nexia-ventas: monto con leyenda "(primer año promoción)"
- [x] nexia-ventas: texto "En breve recibirás acceso a tu app." (antes: "En menos de 12 horas")
- [x] nexia-ventas: logo corregido a Supabase Storage (logo-nexia-white.png)
- [x] NexIA - Activación de Usuarios (n7a + n7b): diseño visual profesional aplicado
      · Header degradado #111827 → #1f2937 con logo transparente desde Supabase Storage
      · Slogan "Digitaliza lo Aburrido" en #00A3FF
      · Fondo #f4f4f4, contenedor blanco con border-radius y sombra
      · Footer gris #f9fafb con nexiasoluciones.com.mx
      · Firma "Equipo NexIA Soluciones"
- [x] NexIA - Activación de Usuarios: acentos corregidos ("rápido", "contraseña")
- [x] Flujo de activación manual (activate_user.sh → webhook nexia-activate) operativo y retorna HTTP 200

## Pendiente crítico ⚠️
- [ ] Verificar rutas /planner /facturacion /tienda en producción tras deploy
- [ ] CORS nexia-notificarme: el webhook falla desde localhost con CORS error. nexia-ventas y nexia-contacto funcionan correctamente. Posible causa: workflow nuevo necesita reinicio de n8n o configuración adicional. Revisar via SSH al VPS: docker restart n8n o verificar headers CORS en el contenedor.

## Pendiente 🔄
- [ ] Verificar hero en mobile — posición del botón CTA
- [x] Logo en correos — resuelto: URL Supabase Storage operativa en todos los workflows
- [x] Imágenes agregadas a cards PDCA, VSM, SMED, Heijunka, Facturación
- [x] npm run build sin errores — build limpio en 6.25s
- [ ] Imagen para card Nexia Tienda (app-nexia-tienda.jpeg)

## Regla — Slug de apps en nexia_billing ⚠️

El campo `appSlug` que se envía al webhook nexia-ventas y se guarda en
`nexia_billing.nexia_subscriptions.app_slug` SIEMPRE es el slug CORTO del
proyecto real del ecosistema, NUNCA el alias visual de la landing page.

**Mapeo activo** (definido en `handleSubmit` de ProductsPage.jsx y AppLanding.jsx):
```js
const slugMap = {
  'nexia-planner':     'scholar',      // NexIA Planner → app nexia-scholar
  'nexia-facturacion': 'facturacion',  // Nexia Gastos  → app nexia-facturacion
  'nexia-tienda':      'tienda',       // Nexia Tienda  → app nexia-tienda
};
```

**Al agregar una nueva app con ctaActive:true:**
1. Agregar entrada al `slugMap` en ProductsPage.jsx → handleSubmit
2. Si tiene ruta dedicada: agregar entrada al `slugMap` en AppLanding.jsx → handleSubmit
3. Actualizar este mapeo en AGENTS.md

## Arquitectura nexia-ventas (n8n) — 2026-05-11 ✅

Workflow `BNlgyXvb1qzwtWUU` — 7 nodos activos:

```
Webhook → Formatear Datos → Preparar UPSERT billing → UPSERT nexia_billing
        → Email Interno → Email al Usuario → Responder 200
```

- **Preparar UPSERT billing**: Code node — construye payload dinámico desde body del webhook
- **UPSERT nexia_billing**: HTTP POST a Supabase con `status: 'prospecto'` y datos de factura si aplica
- El UPSERT ocurre ANTES de los emails — si falla, bloquea el flujo y es detectable
- Email Interno y Email al Usuario referencian "Formatear Datos" por nombre (`$node["Formatear Datos"]`)

## Cambios 2026-05-11 ✅

- [x] BD: 10 columnas nuevas en nexia_billing.nexia_subscriptions (telefono, factura_*)
- [x] BD: columna `factura_enviada boolean DEFAULT false` agregada a nexia_subscriptions
- [x] BD: columna `factura_fecha_envio timestamptz` agregada a nexia_subscriptions
- [x] ProductsPage.jsx: formulario con checkbox factura + campos condicionales + slugMap en handleSubmit
- [x] AppLanding.jsx: idéntico al anterior
- [x] nexia-ventas: sección de facturación en correos (interno siempre visible, usuario condicional con aviso 24h)
- [x] nexia-activate: nodo "Preparar payload" — UPSERT dinámico con campos de facturación y teléfono
- [x] nexia-ventas: UPSERT prospecto en nexia_billing antes de emails (2 nodos nuevos)
- [x] nexia-ventas + nexia-activate: fix UPSERT — URL con `?on_conflict=user_email,app_slug` (evita 409 en segundo intento)

## Workflow nexia-facturacion-recordatorio ✅
- ID: mTY8OCvvXGq4YhYy
- Schedule: 8:00 AM y 4:00 PM hora México (America/Mexico_City)
- Consulta: nexia_billing.nexia_subscriptions WHERE requiere_factura=true AND factura_enviada=false
- Clasifica: Vencidas (>24h), Por vencer (20-24h), Recientes (<20h)
- Envía correo solo si hay urgentes a ventas@ con BCC a daniel.navarro@ y juan.garces@
- Para activar: n8n UI → toggle ON

## Marcar factura como enviada
Ejecutar SQL en Supabase cuando se emita la factura:
```sql
UPDATE nexia_billing.nexia_subscriptions
SET factura_enviada = true, factura_fecha_envio = now()
WHERE user_email = 'email@cliente.com' AND app_slug = 'scholar';
```

## Restricciones activas
- NUNCA modificar copy/textos — están aprobados y liberados
- NUNCA tratar este proyecto como SaaS
- NO git add, git commit, ni git push sin autorización explícita de Daniel
- SIEMPRE incluir dist/ en el commit — Hostinger lo requiere para el deploy vía GIT

## Agente responsable
Vibecoder — cambios visuales únicamente, previa aprobación de Daniel (Vibe Check)
