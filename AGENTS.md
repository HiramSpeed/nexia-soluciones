# AGENTS.md — nexia-soluciones Landing Page
> Estado del proyecto. Actualizar al cerrar cada tarea.
> Última actualización: 2026-05-07

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

## Restricciones activas
- NUNCA modificar copy/textos — están aprobados y liberados
- NUNCA tratar este proyecto como SaaS
- NO git add, git commit, ni git push sin autorización explícita de Daniel
- SIEMPRE incluir dist/ en el commit — Hostinger lo requiere para el deploy vía GIT

## Agente responsable
Vibecoder — cambios visuales únicamente, previa aprobación de Daniel (Vibe Check)
