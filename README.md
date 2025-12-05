# NexIA Soluciones - Landing Page

Landing page profesional para NexIA Soluciones, empresa de automatización con IA.

## 🚀 Inicio Rápido

```bash
# Instalar dependencias
npm install

# Desarrollo local
npm run dev

# Build para producción
npm run build
```

## 📋 Secciones del Sitio

- ✅ **Header**: Navegación con logo y CTA
- ✅ **Hero**: Sección principal con logo grande y CTA
- ✅ **Beneficios**: 3 propuestas de valor clave
- ✅ **Productos**: NexGuard y NexAdmin con mockups
- ✅ **Consultoría**: Soluciones personalizadas de IA
- ✅ **Academia**: Cursos de automatización
- ⏸️ **Testimonios**: TEMPORALMENTE DESHABILITADA (ver nota abajo)
- ✅ **Footer**: Contacto y formulario

## ⚠️ NOTA IMPORTANTE - Sección de Testimonios

La sección **"Nuestros Clientes lo Confirman"** está temporalmente comentada en el código.

**Razón**: Pendiente de autorización de los clientes mencionados.

**Para reactivarla:**
1. Obtener autorización escrita de los clientes
2. Abrir `src/App.jsx`
3. Descomentar las líneas:
   - Línea 8: `import Testimonials from './components/Testimonials';`
   - Líneas 32-34: `<Testimonials />`
4. Guardar y verificar que se muestre correctamente

## 📧 Configuración de Formularios

Los formularios están configurados pero requieren setup de EmailJS:

1. Ver guía completa en: `EMAILJS_SETUP.md`
2. Crear cuenta en EmailJS
3. Configurar credenciales en `src/components/ContactModal.jsx`

**Destinatarios configurados:**
- info@nexiasoluciones.com.mx
- ventas@nexiasoluciones.com.mx

## 🌐 Publicación

Ver guía completa de deployment en: `DEPLOYMENT_GUIDE.md`

**Opciones recomendadas:**
1. **Vercel** (más fácil)
2. Netlify
3. GitHub Pages

## 📁 Estructura del Proyecto

```
nexia-soluciones/
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Hero.jsx
│   │   ├── Benefits.jsx
│   │   ├── Products.jsx
│   │   ├── Consulting.jsx
│   │   ├── Academy.jsx
│   │   ├── Testimonials.jsx (deshabilitado temporalmente)
│   │   ├── Footer.jsx
│   │   ├── Button.jsx
│   │   └── ContactModal.jsx
│   ├── assets/
│   │   ├── logo.png
│   │   ├── nexguard-mockup.png
│   │   └── nexadmin-mockup.png
│   ├── App.jsx
│   └── index.css
├── DEPLOYMENT_GUIDE.md
├── EMAILJS_SETUP.md
└── README.md
```

## 🎨 Tecnologías

- **Framework**: React + Vite
- **Estilos**: CSS Vanilla (inline styles)
- **Fuentes**: Jura (headings), Lato (body)
- **Formularios**: EmailJS (pendiente configuración)

## 📝 Checklist Pre-Deploy

- [ ] Configurar EmailJS
- [ ] Obtener autorización para testimonios
- [ ] Verificar responsive en móvil
- [ ] Probar todos los formularios
- [ ] Configurar dominio personalizado (opcional)

## 📞 Contacto

- **Email General**: info@nexiasoluciones.com.mx
- **Ventas**: ventas@nexiasoluciones.com.mx
- **Soporte**: soporte@nexiasoluciones.com.mx
- **Teléfono**: +(52) 461 180 7955

---

**Última actualización**: Diciembre 2025
