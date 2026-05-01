# 🎨 NexIA Soluciones - Design System

Para mantener la consistencia visual ("look & feel") en la nueva aplicación, utilicen los siguientes tokens de diseño.

## 1. Variables CSS Globales
Copia este bloque en tu archivo CSS raíz (`:root`) para heredar todos los colores y tipografías.

```css
:root {
  /* Marca */
  --primary-color: #00A3FF;       /* Azul Tech Vibrante */
  --primary-hover: #0081CC;       /* Estado Hover */

  /* Fondos */
  --background-color: #1a202c;    /* Azul Oscuro Profundo (Fondo Main) */
  --card-background: #2d3748;     /* Gris Azulado (Tarjetas/Paneles) */

  /* Textos */
  --text-color: #FFFFFF;          /* Blanco Puro (Títulos/Body Main) */
  --secondary-text-color: #E2E8F0; /* Blanco Hueso (Subtítulos/Texto Secundario) */

  /* Tipografía */
  --font-main: 'Lato', sans-serif;  /* Cuerpo de texto */
  --font-heading: 'Jura', sans-serif; /* Títulos, Botones, Navegación */
}
```

## 2. Tipografías (Google Fonts)
Asegúrate de importar estas fuentes en el `<head>` de tu `index.html` o en tu CSS:

```html
<link href="https://fonts.googleapis.com/css2?family=Jura:wght@300;400;500;600;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
```

## 3. Estilos Base (Recomendados)
Para que los elementos básicos se sientan igual:

```css
body {
  font-family: var(--font-main);
  background-color: var(--background-color);
  color: var(--text-color);
  line-height: 1.6;
}

h1, h2, h3, h4, buttons {
  font-family: var(--font-heading);
}

button {
  cursor: pointer;
  border: none;
  background-color: var(--primary-color);
  color: white;
  border-radius: 8px; /* Radio de borde estándar */
}
```

## 4. Archivo Fuente Completo
El archivo CSS completo de la landing page se encuentra en:
`src/index.css`
