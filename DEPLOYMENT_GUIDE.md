# 🚀 Guía de Publicación - NexIA Soluciones

## Opción 1: Vercel (RECOMENDADO - Más Fácil)

### ✅ Ventajas
- ✅ **Gratis** para proyectos personales
- ✅ **Dominio gratis**: `tu-sitio.vercel.app`
- ✅ **Deploy automático** desde GitHub
- ✅ **SSL/HTTPS** incluido
- ✅ **Actualizaciones automáticas** al hacer push a GitHub

### 📋 Pasos para Publicar en Vercel

#### 1. Preparar el Proyecto
```bash
# Asegúrate de estar en la carpeta del proyecto
cd C:\Users\dhira\.gemini\antigravity\scratch\nexia-soluciones

# Verifica que todo funcione
npm run build
```

#### 2. Subir a GitHub
```bash
# Inicializar Git (si no lo has hecho)
git init

# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "Initial commit - NexIA Soluciones landing page"

# Crear repositorio en GitHub:
# - Ve a https://github.com/new
# - Nombre: nexia-soluciones
# - Visibilidad: Público o Privado
# - NO inicialices con README

# Conectar con GitHub (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/nexia-soluciones.git
git branch -M main
git push -u origin main
```

#### 3. Deploy en Vercel
1. Ve a [https://vercel.com](https://vercel.com)
2. Haz clic en **"Sign Up"** o **"Log In"** (usa tu cuenta de GitHub)
3. Haz clic en **"Add New Project"**
4. Selecciona tu repositorio `nexia-soluciones`
5. Vercel detectará automáticamente que es un proyecto Vite
6. Haz clic en **"Deploy"**
7. ¡Listo! En 1-2 minutos tu sitio estará en línea

#### 4. Configurar Dominio Personalizado (Opcional)
Si tienes `nexiasoluciones.com.mx`:
1. En Vercel, ve a tu proyecto > **Settings** > **Domains**
2. Agrega tu dominio
3. Sigue las instrucciones para configurar los DNS

---

## Opción 2: Netlify (Alternativa Fácil)

### 📋 Pasos para Netlify

#### Deploy Directo (Sin GitHub)
1. Ve a [https://www.netlify.com](https://www.netlify.com)
2. Crea una cuenta
3. Arrastra la carpeta `dist` (después de hacer `npm run build`) al área de deploy
4. ¡Listo!

#### Deploy con GitHub (Recomendado)
1. Sube tu proyecto a GitHub (ver pasos arriba)
2. En Netlify, haz clic en **"Add new site"** > **"Import an existing project"**
3. Conecta con GitHub
4. Selecciona tu repositorio
5. Build command: `npm run build`
6. Publish directory: `dist`
7. Haz clic en **"Deploy"**

---

## Opción 3: GitHub Pages (Gratis pero más pasos)

### 📋 Pasos para GitHub Pages

#### 1. Instalar gh-pages
```bash
npm install --save-dev gh-pages
```

#### 2. Actualizar package.json
Agrega estas líneas en `package.json`:
```json
{
  "homepage": "https://TU_USUARIO.github.io/nexia-soluciones",
  "scripts": {
    "predeploy": "npm run build",
    "deploy": "gh-pages -d dist"
  }
}
```

#### 3. Actualizar vite.config.js
```javascript
export default defineConfig({
  base: '/nexia-soluciones/',
  plugins: [react()],
})
```

#### 4. Deploy
```bash
npm run deploy
```

---

## 🎯 Recomendación Final

**Para NexIA Soluciones, te recomiendo Vercel porque:**
1. ✅ Es el más fácil (3 clics después de subir a GitHub)
2. ✅ Deploy automático (cada vez que hagas cambios)
3. ✅ Mejor rendimiento
4. ✅ Fácil configurar dominio personalizado
5. ✅ Analytics gratis

---

## 📝 Checklist Antes de Publicar

- [ ] Configurar EmailJS (o servicio de formularios)
- [ ] Reemplazar imágenes placeholder si las hay
- [ ] Verificar que todos los links funcionen
- [ ] Probar el sitio en móvil (responsive)
- [ ] Agregar Google Analytics (opcional)
- [ ] Configurar dominio personalizado (opcional)

---

## 🔧 Comandos Útiles

```bash
# Desarrollo local
npm run dev

# Crear build de producción
npm run build

# Preview del build
npm run preview

# Ver el build localmente antes de publicar
npm run build && npm run preview
```

---

## 🌐 URLs Finales

Después de publicar tendrás:
- **Vercel**: `https://nexia-soluciones.vercel.app`
- **Netlify**: `https://nexia-soluciones.netlify.app`
- **Dominio propio**: `https://nexiasoluciones.com.mx` (si lo configuras)

---

## ❓ ¿Necesitas Ayuda?

Si tienes problemas:
1. Revisa la consola de errores en Vercel/Netlify
2. Asegúrate de que `npm run build` funcione localmente
3. Verifica que todas las dependencias estén en `package.json`
