# 📧 Configuración Rápida de Formspree (5 minutos)

Formspree es más fácil que EmailJS - solo necesitas un email.

## Pasos para Activar el Formulario

### 1. Crear Cuenta en Formspree
1. Ve a: https://formspree.io/register
2. Regístrate con tu email (gratis para 50 envíos/mes)
3. Confirma tu email

### 2. Crear un Nuevo Formulario
1. Haz clic en **"+ New Form"**
2. **Form Name**: "NexIA Soluciones - Contacto"
3. **Email**: `info@nexiasoluciones.com.mx` (aquí llegarán los mensajes)
4. Haz clic en **"Create Form"**

### 3. Copiar el Form ID
Verás algo como: `https://formspree.io/f/xyzabc123`

El **Form ID** es la parte después de `/f/`: `xyzabc123`

### 4. Actualizar el Código
1. Abre: `src/components/ContactModal.jsx`
2. Busca la línea 28: `https://formspree.io/f/YOUR_FORM_ID`
3. Reemplaza `YOUR_FORM_ID` con tu Form ID
4. Ejemplo: `https://formspree.io/f/xyzabc123`

### 5. Configurar Emails Adicionales (Opcional)
Si quieres que los emails también lleguen a `ventas@nexiasoluciones.com.mx`:

1. En Formspree, ve a tu formulario
2. Click en **Settings** > **Notifications**
3. Agrega `ventas@nexiasoluciones.com.mx` en "Additional Recipients"

### 6. Subir Cambios a Vercel
```bash
git add .
git commit -m "Configurar Formspree para formularios"
git push
```

Vercel detectará el cambio y actualizará automáticamente en 1-2 minutos.

## ✅ Verificar que Funciona

1. Ve a tu sitio en Vercel
2. Haz clic en cualquier botón CTA
3. Llena el formulario de prueba
4. Envía
5. Revisa tu email `info@nexiasoluciones.com.mx`

## 🎯 Ventajas de Formspree vs EmailJS

- ✅ **Más fácil**: Solo necesitas un Form ID
- ✅ **Más rápido**: 5 minutos vs 20 minutos
- ✅ **Más confiable**: Menos configuración = menos errores
- ✅ **Spam protection** incluido
- ✅ **Email notifications** automáticas

## 📊 Plan Gratuito

- ✅ 50 envíos/mes
- ✅ Notificaciones por email
- ✅ Sin marca de agua
- ✅ Protección anti-spam

Si necesitas más, el plan pagado es $10/mes para 1000 envíos.

## ❓ Problemas Comunes

**Error 403**: Verifica que el Form ID sea correcto
**No llegan emails**: Revisa spam y confirma tu email en Formspree
**Error CORS**: Asegúrate de usar `https://formspree.io/f/...` (con la f)

---

**Tiempo total de configuración: ~5 minutos** ⚡
