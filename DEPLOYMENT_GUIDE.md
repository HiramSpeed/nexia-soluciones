# 🚀 Guía de Publicación en Vercel - NexIA Soluciones

Tu proyecto **ya está actualizado en GitHub**. Ahora sigue estos pasos sencillos para desplegarlo en Vercel.

## 1. Crear Cuenta / Iniciar Sesión en Vercel
1. Ve a [https://vercel.com](https://vercel.com)
2. Haz clic en **"Sign Up"** (si no tienes cuenta) o **"Log In"**.
3. **IMPORTANTE**: Elige **"Continue with GitHub"** y usa la misma cuenta donde tienes el repositorio `nexia-soluciones`.

## 2. Importar el Proyecto
1. En tu Dashboard de Vercel, haz clic en el botón blanco **"Add New..."** (arriba a la derecha) y selecciona **"Project"**.
2. Verás una lista de tus repositorios de GitHub. Busca **`nexia-soluciones`**.
3. Haz clic en el botón **"Import"** junto a ese nombre.

## 3. Configurar y Desplegar
Verás una pantalla de configuración ("Configure Project"):
1. **Framework Preset**: Vercel detectará automáticamente **Vite**. Déjalo así.
2. **Root Directory**: Déjalo en `./`
3. **Environment Variables**: No necesitas configurar ninguna variable de entorno por ahora (a menos que uses claves privadas para EmailJS, pero si están en el código funcionarán igual por ahora).
4. Haz clic en el botón azul **"Deploy"**.

## 4. ¡Listo! 🎉
- Vercel comenzará a "construir" (build) tu sitio. Verás logs en pantalla.
- En aproximadamente 1 minuto, verás confeti y un mensaje de **"Congratulations!"**.
- Haz clic en la imagen de vista previa o el botón **"Visit"** para ver tu sitio en vivo.
- **Tu URL será algo como:** `nexia-soluciones.vercel.app`.

---

## 🔄 Actualizaciones Futuras

¡Ya no tienes que hacer nada manual en Vercel!
Como ya está conectado a GitHub, **cada vez que yo (tu asistente IA) o tú hagamos un `git push` con cambios**, Vercel detectará la actualización y volverá a publicar el sitio automáticamente en cuestión de segundos.

---

## 🌐 Configurar Dominio Personalizado (.com.mx)

Si ya compraste tu dominio `nexiasoluciones.com.mx`:
1. En tu proyecto en Vercel, ve a la pestaña **Settings** (arriba).
2. En el menú izquierdo, selecciona **Domains**.
3. Escribe `nexiasoluciones.com.mx` en el campo de entrada y haz clic en **Add**.
4. Vercel te dará unos registros DNS (tipo A o CNAME) que debes copiar.
5. Ve a tu proveedor de dominio (donde lo compraste, ej. GoDaddy, Namecheap, Akky) y pega esos registros en la configuración DNS de tu dominio.
6. Espera unos minutos (o hasta 24h) y tu sitio estará seguro (HTTPS) en tu propio dominio.
