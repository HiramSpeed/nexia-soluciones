# 🔄 Cómo Retomar el Proyecto NexIA Soluciones

## 📂 Ubicación del Proyecto

**Ruta Local**: `C:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones`

---

## 🚀 Para Continuar Trabajando Mañana

### **Opción 1: Abrir en VS Code (o tu editor)**

1. Abre VS Code
2. File → Open Folder
3. Navega a: `C:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones`
4. Abre la terminal integrada (Ctrl + `)
5. Ejecuta:
   ```bash
   npm run dev
   ```
6. Abre: http://localhost:5173

### **Opción 2: Usar Antigravity**

Cuando vuelvas a usar Antigravity, simplemente dile:

> "Quiero continuar con el proyecto NexIA Soluciones que está en `C:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones`"

Antigravity recordará el contexto y podrás seguir trabajando.

---

## 🌐 Enlaces Importantes

- **Sitio en Vivo**: Ve a Vercel → https://vercel.com (tu proyecto)
- **GitHub**: https://github.com/HiramSpeed/nexia-soluciones
- **Formspree**: https://formspree.io (gestión de formularios)

---

## 📝 Estado Actual del Proyecto

✅ **Completado:**
- Landing page diseñada y publicada
- Logo integrado (grande en Hero, visible en Header)
- Mockups de NexGuard y NexAdmin
- 5 botones CTA conectados al formulario modal
- Formularios funcionando con Formspree
- Emails llegando a `info@nexiasoluciones.com.mx`
- Código en GitHub con respaldo automático
- Deploy automático en Vercel

⏸️ **Pendiente:**
- Testimonios deshabilitados (esperando autorización)
- Agregar `ventas@nexiasoluciones.com.mx` como destinatario adicional (opcional)
- Configurar dominio personalizado (opcional)

---

## 🔧 Comandos Útiles

```bash
# Iniciar servidor de desarrollo
npm run dev

# Ver cambios antes de publicar
npm run build
npm run preview

# Subir cambios a GitHub/Vercel
git add .
git commit -m "Descripción del cambio"
git push
```

---

## 📋 Tareas Comunes

### **Hacer cambios y publicar:**
1. Edita los archivos que necesites
2. Prueba localmente: `npm run dev`
3. Sube a GitHub:
   ```bash
   git add .
   git commit -m "Descripción"
   git push
   ```
4. Vercel actualiza automáticamente en 1-2 minutos

### **Reactivar Testimonios:**
1. Abre `src/App.jsx`
2. Línea 8: Descomenta `import Testimonials...`
3. Líneas 32-34: Descomenta `<Testimonials />`
4. Sube cambios con `git push`

### **Cambiar contenido:**
- **Textos**: Edita los componentes en `src/components/`
- **Imágenes**: Reemplaza en `src/assets/`
- **Colores**: Modifica `src/index.css` (variables CSS)

---

## 🆘 Si Algo Sale Mal

**Perdiste los archivos locales:**
```bash
git clone https://github.com/HiramSpeed/nexia-soluciones.git
cd nexia-soluciones
npm install
npm run dev
```

**El sitio no actualiza en Vercel:**
- Ve a Vercel → Tu proyecto → Deployments
- Verifica que el último deploy haya sido exitoso
- Si falló, revisa los logs

**Problemas con el formulario:**
- Verifica que el Form ID en `ContactModal.jsx` sea: `mldqlnzy`
- Revisa que Formspree esté activo en: https://formspree.io

---

## 📞 Información de Contacto del Sitio

- **Email General**: info@nexiasoluciones.com.mx
- **Ventas**: ventas@nexiasoluciones.com.mx
- **Soporte**: soporte@nexiasoluciones.com.mx
- **Teléfono**: +(52) 461 180 7955

---

**¡Tu proyecto está listo y funcionando!** 🎉

Cualquier cambio que hagas localmente, solo súbelo con `git push` y Vercel lo publicará automáticamente.
