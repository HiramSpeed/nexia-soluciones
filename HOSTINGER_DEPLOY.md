# 🚀 Guía de Despliegue en Hostinger

Desplegar tu aplicación React (Vite) en Hostinger es sencillo. Tienes dos formas principales de hacerlo:

## Opción A: Conexión Automática con Git (Recomendada)
Esta es la mejor opción porque cada vez que hagas `git push`, tu sitio se actualizará solo.

1.  Ve a tu **Panel de Control de Hostinger** (hpanel).
2.  Busca la sección **Sitio Web** -> **Git**.
3.  Agrega tu repositorio:
    *   **Repository**: `HiramSpeed/nexia-soluciones` (o la URL completa).
    *   **Branch**: `main`.
    *   **Directory**: déjalo en blanco (o `public_html` si te lo pide y es la única app).
4.  Hostinger clonará tu proyecto.
5.  **IMPORTANTE (Build Step)**:
    *   Como es un proyecto de React, Hostinger necesita "construirlo".
    *   Si tienes acceso SSH o Terminal en Hostinger, entra y ejecuta:
        ```bash
        cd public_html
        npm install
        npm run build
        ```
    *   *Nota: El hosting compartido a veces complica correr Node.js. Si esto falla, usa la Opción B.*

---

## Opción B: Subida Manual (Infalible)
Esta opción funciona en cualquier plan de hosting (Shared, Cloud, etc.) porque solo subes los archivos finales estáticos.

### 1. Preparar los archivos (En tu computadora)
Yo (tu Asistente) ya he preparado el proyecto. Solo necesitas generar la versión final:

1.  Abre tu terminal en VS Code y ejecuta:
    ```bash
    npm run build
    ```
2.  Esto creará una carpeta llamada **`dist`** en tu proyecto.
    *   Esta carpeta contiene todo: `index.html`, tus imágenes, el `.htaccess` (que acabo de crear para que funcionen las rutas), etc.

### 2. Subir a Hostinger
1.  Ve a tu **HPanel** -> **Administrador de Archivos** (Files).
2.  Entra a la carpeta **`public_html`**.
3.  Borra el archivo `default.php` si existe.
4.  Sube **TODO el contenido** que está DENTRO de la carpeta `dist` (no subas la carpeta `dist`, sube lo que hay adentro).
    *   Deberías ver `index.html`, la carpeta `assets`, `.htaccess`, etc., directamente en `public_html`.

### 3. ¡Listo!
Visita tu dominio (ej. `nexiasoluciones.com`) y verás tu sitio funcionar.

---

## 🔧 Solución de Problemas Comunes

**Error 404 al recargar la página:**
Si entras a `tudominio.com/contacto` y recargas, ¿sale error?
*   ✅ **Solución**: Asegúrate de haber subido el archivo `.htaccess` que acabo de crear en la carpeta `public`. Este archivo le dice al servidor "si no encuentras el archivo, carga index.html" (necesario para React).

**Cambios no se ven:**
*   Borra la caché de tu navegador o del hosting (si tienes Cloudflare o caché de Hostinger activada).
