# AGENTS.md — nexia-soluciones Landing Page
> Estado del proyecto. Actualizar al cerrar cada tarea.
> Última actualización: 2026-04-22

## Estado actual
Landing page single-page con scroll continuo. Hero reemplazado por imagen completa con botón CTA dorado superpuesto. Todos los correos migrados a Resend via n8n (nexia-ventas + nexia-contacto) con BCC a daniel.navarro@ y juan.garces@. Rama feature/scroll-continuo lista para review y merge.

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

## Pendiente crítico ⚠️
- [ ] Merge feature/scroll-continuo → main cuando Daniel apruebe
- [ ] Deploy a Hostinger
- [ ] CORS nexia-notificarme: el webhook falla desde localhost con CORS error. nexia-ventas y nexia-contacto funcionan correctamente. Posible causa: workflow nuevo necesita reinicio de n8n o configuración adicional. Revisar via SSH al VPS: docker restart n8n o verificar headers CORS en el contenedor.

## Pendiente 🔄
- [ ] Verificar hero en mobile — posición del botón CTA
- [ ] Logo en correos — pendiente URL pública funcional (nexiasoluciones.com.mx/assets/logo-nexia-white.png)
- [x] Imágenes agregadas a cards PDCA, VSM, SMED, Heijunka, Facturación
- [x] npm run build sin errores — build limpio en 6.25s
- [ ] Imagen para card Nexia Tienda (app-nexia-tienda.jpeg)

## Restricciones activas
- NUNCA git push a main — deploy es manual vía Hostinger
- NUNCA modificar copy/textos — están aprobados y liberados
- NUNCA tratar este proyecto como SaaS
- NO git add, git commit, ni git push sin autorización explícita de Daniel

## Agente responsable
Vibecoder — cambios visuales únicamente, previa aprobación de Daniel (Vibe Check)
