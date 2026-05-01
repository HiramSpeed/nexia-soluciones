# CLAUDE.md — nexia-soluciones (Landing Page Corporativa)

## ⚠️ ADVERTENCIAS CRÍTICAS
- **RAMA DE TRABAJO ACTIVA: feature/scroll-continuo** — TODOS los commits y pushes van a esta rama. NUNCA hacer push a main directamente. main = producción en Hostinger.
- **NUNCA ejecutar git push** — producción está en Hostinger, deploy es manual
- **NUNCA modificar textos de contenido** — todos los copies están aprobados y liberados
- **NUNCA ser creativo con el copy** — solo cambios técnicos/visuales aprobados por Daniel
- **NUNCA aplicar patrones de nexia-pdca o nexia-scholar** — este NO es una app SaaS

## Qué es este proyecto
Landing page corporativa de NexIA Soluciones.
URL producción: nexiasoluciones.com.mx
Deploy: Manual vía Hostinger (subida de archivos)
NO usa Supabase, NO usa auth, NO es SaaS.

## Stack
- React 19 + Vite 7
- React Router DOM v7
- CSS puro con variables CSS (sin Tailwind)
- Sin backend, sin base de datos

## Colores corporativos
- --primary-color: #00A3FF (Tech Blue)
- --primary-hover: #0081CC
- --background-color: #1a202c (Dark Blue/Grey)
- --card-background: #2d3748
- --text-color: #FFFFFF
- --font-main: 'Lato', sans-serif
- --font-heading: 'Jura', sans-serif

## Estructura
src/
  App.jsx           ← Router principal
  index.css         ← Variables globales y estilos base
  components/
    Header.jsx
    Hero.jsx
    Footer.jsx
    ContactModal.jsx
    ... (ver ls src/components/)

## Protocolo de trabajo
1. Mostrar EXACTAMENTE qué vas a cambiar antes de tocar cualquier archivo
2. Esperar confirmación de Daniel (Vibe Check)
3. Solo después de confirmación → aplicar cambio
4. NO hacer git add, git commit, ni git push sin autorización explícita
5. Cambios mínimos necesarios — nada más

## Estándar — Sección Productos (Cards de Apps)

### Estructura de una card de app
Cada app del ecosistema Nexia sigue este patrón exacto en ProductsPage.jsx:

```js
{
  id: 1,
  slug: 'nexia-planner',           // identificador único
  title: 'Nexia Planner',          // nombre de la app
  subtitle: 'Planificador Académico', // subtítulo descriptivo
  image: appNexiaPlanner,          // import desde src/assets/app-{slug}.jpeg
  badge: 'EN PRODUCCIÓN',          // EN PRODUCCIÓN | BETA | PRÓXIMAMENTE
  badgeColor: '#22c55e',           // verde=producción, amarillo=beta, gris=próximo
  price: '$280 MXN / año',         // precio oficial
  priceLabel: 'Precio de lanzamiento',
  features: [                      // máximo 5 features
    'Organización sin estrés',
    'Cálculos instantáneos',
    'Comunicación rápida',
    'Sin complicaciones técnicas',
    'Uso inmediato'
  ],
  ctaActive: true,                 // true = botón azul activo
  ctaLabel: 'Quiero esta app',     // texto del botón principal
  onlinePayment: false,            // false = botón gris deshabilitado
}
```

### Para agregar una nueva app:
1. Copiar imagen a src/assets/app-{slug}.jpeg
2. Agregar objeto al array products[] siguiendo el patrón
3. Si ctaActive=true → abre PurchaseModal con app pre-seleccionada
4. Si onlinePayment=true → activar botón Lemon Squeezy con URL real

### Formulario de compra — patrón activo
El formulario de compra está INLINE en la card — NO usar modales separados.
PurchaseModal.jsx existe en disco pero está deprecado.
El componente estándar es ProductsPage.jsx con expandedCard state:
- expandedCard: id de la card abierta | null
- Al expandir: card sube a z-index 101, overlay fijo rgba(0,0,0,0.7) a z-index 100
- Formulario aparece debajo del precio con hr azul separador
- POST a VITE_N8N_VENTAS_WEBHOOK con { appName, appPrice, nombre, email, telefono, mensaje }

### Tabs y navegación
- Tab por defecto: 'todos'
- Reset al navegar: hashchange a #productos resetea a 'todos'
- Para nuevo grupo: agregar objeto a groups[] con id, label, products[]
- Imágenes de apps: src/assets/app-{slug}.jpeg

### Naming de assets
- app-nexia-planner.jpeg
- app-nexia-pdca.jpeg
- app-nexia-vsm.jpeg
- app-nexia-scholar.jpeg (mismo que planner)
- app-nexia-heijunka.jpeg
- app-nexia-smed.jpeg
