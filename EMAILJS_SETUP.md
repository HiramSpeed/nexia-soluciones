# Configuración de EmailJS para Formularios de Contacto

## 📧 Pasos para Configurar EmailJS

### 1. Crear Cuenta en EmailJS
1. Ve a [https://www.emailjs.com/](https://www.emailjs.com/)
2. Crea una cuenta gratuita (permite 200 emails/mes)

### 2. Configurar Servicio de Email
1. En el dashboard, ve a **Email Services**
2. Haz clic en **Add New Service**
3. Selecciona tu proveedor de email (Gmail, Outlook, etc.)
4. Conecta tu cuenta
5. Copia el **Service ID** (ejemplo: `service_abc123`)

### 3. Crear Template de Email
1. Ve a **Email Templates**
2. Haz clic en **Create New Template**
3. Usa este template:

```
Asunto: Nuevo Lead desde NexIA Soluciones - {{source}}

Nombre: {{from_name}}
Email: {{from_email}}
Teléfono: {{phone}}
Origen: {{source}}

Mensaje:
{{message}}
```

4. Copia el **Template ID** (ejemplo: `template_xyz789`)

### 4. Obtener Public Key
1. Ve a **Account** > **General**
2. Copia tu **Public Key** (ejemplo: `abc123XYZ`)

### 5. Actualizar el Código
Abre `src/components/ContactModal.jsx` y reemplaza las siguientes líneas (líneas 28-30):

```javascript
service_id: 'YOUR_SERVICE_ID',      // Reemplaza con tu Service ID
template_id: 'YOUR_TEMPLATE_ID',    // Reemplaza con tu Template ID
user_id: 'YOUR_PUBLIC_KEY',         // Reemplaza con tu Public Key
```

### 6. Configurar Destinatarios
Los emails se enviarán automáticamente a:
- info@nexiasoluciones.com.mx
- ventas@nexiasoluciones.com.mx

Esto ya está configurado en el código (línea 31 de ContactModal.jsx).

## ✅ Verificación
1. Guarda los cambios
2. Prueba el formulario desde cualquier botón CTA
3. Verifica que recibas el email en ambas direcciones

## 🎯 Botones Conectados
Todos estos botones abren el formulario modal:
- ✅ Auditoría Gratuita (Header)
- ✅ Quiero mi Auditoría Gratuita de IA (Hero)
- ✅ Explorar Nuestras Apps (Productos)
- ✅ Solicitar una Llamada Estratégica (Consultoría)
- ✅ Descargar Guía Gratuita (Academia)

El formulario del Footer también incluye el campo de celular.

## 📝 Campos del Formulario
- Nombre Completo *
- Correo Electrónico *
- Celular *
- Mensaje / Comentarios
- Origen (campo oculto que identifica de dónde vino el lead)

## 🔄 Alternativa: Usar un Backend Propio
Si prefieres no usar EmailJS, puedes:
1. Crear un endpoint en tu servidor (Node.js, PHP, etc.)
2. Actualizar la función `handleSubmit` en `ContactModal.jsx` para enviar a tu endpoint
3. Configurar el envío de emails desde tu servidor
