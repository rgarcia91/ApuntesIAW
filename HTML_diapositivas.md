---
marp: true
theme: default
paginate: true
backgroundImage: url('img/fondo.png')
header: Implantación de aplicaciones Web. Tema 1 Repaso HTML - CSS - Javascript.
footer: IES Camp de Morvedre - Curso 24/25
---

# Módulos:
* Introducción a HTML
* Texto y Enlaces en HTML
* Imágenes y Multimedia en HTML
* Introducción a CSS
* Estilización de Texto y Fondos en CSS
* Diseño de Layouts con CSS
* Introducción a JavaScript
* Manipulación del DOM con JavaScript
* Introducción a Bootstrap
* Proyecto Final

---

# Introducción a HTML

---

## ¿Qué es HTML?

- HTML significa **HyperText Markup Language**.
- Es el estándar para crear páginas web.
- Utiliza **etiquetas** para estructurar el contenido.

---

## Estructura básica de un documento HTML
```html
<!DOCTYPE html>
<html>
<head>
  <title>Mi Primera Página</title>
</head>
<body>
  <h1>¡Hola, Mundo!</h1>
  <p>Esta es mi primera página HTML.</p>
</body>
</html>
```

---
## Etiquetas esenciales

- `<html>`: Contenedor principal de todo el documento.
- `<head>`: Contiene metadatos y el título de la página.
- `<body>`: Contiene el contenido visible de la página.
- `<title>`: Define el título de la página que aparece en la pestaña del navegador.

---


# Texto y Enlaces en HTML

---

## Etiquetas de Texto

- `<h1>` a `<h6>`: Encabezados de diferentes niveles.
- `<p>`: Párrafo.
- `<strong>`: Texto en negrita.
- `<em>`: Texto en cursiva.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Texto</title>
</head>
<body>
  <h1>Encabezado 1</h1>
  <h2>Encabezado 2</h2>
  <p>Este es un párrafo.</p>
  <p><strong>Texto en negrita</strong> y <em>texto en cursiva</em>.</p>
</body>
</html>
```

---

## Listas

- `<ul>`: Lista desordenada.
- `<ol>`: Lista ordenada.
- `<li>`: Elemento de lista.

---

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Listas</title>
</head>
<body>
  <h1>Lista Desordenada</h1>
  <ul>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
  </ul>
  <h1>Lista Ordenada</h1>
  <ol>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
  </ol>
</body>
</html>
```

---

## Enlaces

- `<a>`: Define un hipervínculo.
  - `href`: Especifica la URL del enlace.
  - `target`: Define dónde abrir el enlace (por ejemplo, `_blank` para una nueva pestaña).

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Enlaces</title>
</head>
<body>
  <p>Visita <a href="https://www.example.com" target="_blank">Example</a> para más información.</p>
</body>
</html>
```

# Imágenes y Multimedia en HTML

---

## Imágenes

- `<img>`: Etiqueta para insertar imágenes.
  - `src`: Especifica la ruta de la imagen.
  - `alt`: Texto alternativo para la imagen.
  - `width` y `height`: Especifican el tamaño de la imagen.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Imágenes</title>
</head>
<body>
  <h1>Imagen de Ejemplo</h1>
  <img src="ruta/a/tu/imagen.jpg" alt="Descripción de la imagen" width="500" height="300">
</body>
</html>
```
---

## Videos

- `<video>`: Etiqueta para insertar videos.
  - `src`: Especifica la ruta del video.
  - `controls`: Muestra controles de reproducción.
  - `autoplay`: Reproduce el video automáticamente.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Videos</title>
</head>
<body>
  <h1>Video de Ejemplo</h1>
  <video src="ruta/a/tu/video.mp4" controls width="600" height="400"></video>
</body>
</html>
```

---

## Audio

- `<audio>`: Etiqueta para insertar archivos de audio.
  - `src`: Especifica la ruta del archivo de audio.
  - `controls`: Muestra controles de reproducción.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Audio</title>
</head>
<body>
  <h1>Audio de Ejemplo</h1>
  <audio src="ruta/a/tu/audio.mp3" controls></audio>
</body>
</html>
```

# Introducción a CSS

---

## ¿Qué es CSS?

- CSS significa **Cascading Style Sheets**.
- Es el lenguaje utilizado para describir la presentación de documentos HTML.
- Permite separar el contenido de la presentación.

---

## Sintaxis Básica de CSS

- Selectores: Indican a qué elementos HTML se aplicarán los estilos.
- Propiedades: Definen qué aspecto del elemento se va a estilizar.
- Valores: Especifican cómo se aplicará la propiedad.
---

```css
/* Selector de elemento */
p {
  color: blue;
  font-size: 16px;
}

/* Selector de clase */
.intro {
  margin: 20px;
  padding: 10px;
}

/* Selector de ID */
#main {
  background-color: lightgray;
  border: 1px solid black;
}
```
---

## Selectores y Propiedades

- Selectores: `elemento`, `.clase`, `#id`.
- Propiedades comunes: `color`, `font-size`, `margin`, `padding`.

---


```html
<!DOCTYPE html>
<html>
<head>
  <style>
    p {
      color: blue;
      font-size: 16px;
    }
    .intro {
      margin: 20px;
      padding: 10px;
    }
    #main {
      background-color: lightgray;
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <p class="intro">Este es un párrafo con clase "intro".</p>
  <div id="main">
    <p>Este es un párrafo dentro de un div con ID "main".</p>
  </div>
</body>
</html>
```
---
## Aplicación de CSS

- Inline: Dentro de la etiqueta HTML.
- Interno: Dentro de una etiqueta `<style>` en el `<head>`.
- Externo: En un archivo `.css` separado.

---

## Ejemplo de CSS inline

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <title>Ejemplo Sencillo de CSS</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f0f0f0; margin: 0; padding: 20px;">
  <h1 style="color: #333; text-align: center;">Hola Mundo</h1>
  <p style="color: #666; font-size: 18px; line-height: 1.6;">
    Este es un ejemplo sencillo de cómo incluir CSS directamente en cada etiqueta HTML utilizando el atributo <code>style</code>.
  </p>
</body>
</html>
```

---

## Ejemplo de CSS interno

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <title>Ejemplo Sencillo de CSS</title>
  <style>
    /* Estilos CSS dentro de la etiqueta <style> */
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
      margin: 0;
      padding: 20px;
    }
    h1 {
      color: #333;
      text-align: center;
    }
    p {
      color: #666;
      font-size: 18px;
      line-height: 1.6;
    }
  </style>
</head>
<body>
  <h1>Hola Mundo</h1>
  <p>Este es un ejemplo sencillo de cómo incluir CSS dentro de una etiqueta <style> en un documento HTML.</p>
</body>
</html>
```
---

## Ejemplo aplicacion CSS externo

```css
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <p class="intro">Este es un párrafo con clase "intro".</p>
  <div id="main">
    <p>Este es un párrafo dentro de un div con ID "main".</p>
  </div>
</body>
</html>
```

---

## Uso de `<div>` para Estructurar Contenido

- `<div>`: Etiqueta de contenedor genérica.
- Utilizada para agrupar elementos y aplicar estilos comunes.

---

## Ejemplo con div
```css
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      width: 80%;
      margin: auto;
      border: 1px solid black;
      padding: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Encabezado Principal</h1>
    <p>Este es un párrafo dentro de un contenedor div.</p>
  </div>
</body>
</html>
```

---

# Estilización de Texto y Fondos en CSS

---

## Propiedades de Texto

- `font-family`: Define la fuente del texto.
- `font-size`: Define el tamaño del texto.
- `color`: Define el color del texto.
- `text-align`: Alinea el texto (left, right, center, justify).

---

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    h1 {
      font-size: 2em;
      color: navy;
      text-align: center;
    }
    p {
      font-size: 1em;
      color: gray;
      text-align: justify;
    }
  </style>
</head>
<body>
  <h1>Encabezado Principal</h1>
  <p>Este es un párrafo con estilos de texto aplicados.</p>
</body>
</html>
```

---

## Fondos

- `background-color`: Define el color de fondo.
- `background-image`: Define una imagen de fondo.
- `background-repeat`: Define si la imagen de fondo se repite (repeat, no-repeat, repeat-x, repeat-y).

---

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background-color: lightblue;
    }
    .container {
      background-image: url('ruta/a/tu/imagen.jpg');
      background-repeat: no-repeat;
      background-size: cover;
      padding: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Encabezado con Fondo</h1>
    <p>Este es un párrafo dentro de un contenedor con una imagen de fondo.</p>
  </div>
</body>
</html>
```

---

# Diseño de Layouts con CSS

---


## Modelo de Caja

- `margin`: Espacio exterior alrededor del elemento.
- `padding`: Espacio interior dentro del elemento.
- `border`: Borde alrededor del elemento.

---

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .box {
      width: 200px;
      height: 100px;
      margin: 20px;
      padding: 10px;
      border: 2px solid black;
      background-color: lightgray;
    }
  </style>
</head>
<body>
  <div class="box">Este es un ejemplo del modelo de caja.</div>
</body>
</html>
```

---

## Diseño de Layouts: Display y Position

- `display`: Define cómo se muestra un elemento (block, inline, inline-block, none).
- `position`: Define la posición de un elemento (static, relative, absolute, fixed, sticky).

---
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .block {
      display: block;
      width: 100%;
      background-color: lightblue;
    }
    .inline {
      display: inline;
      background-color: lightgreen;
    }
    .relative {
      position: relative;
      top: 10px;
      left: 10px;
      background-color: lightcoral;
    }
    .absolute {
      position: absolute;
      top: 50px;
      left: 50px;
      background-color: lightgoldenrodyellow;
    }
  </style>
</head>
<body>
  <div class="block">Elemento block</div>
  <span class="inline">Elemento inline</span>
  <div class="relative">Elemento relative</div>
  <div class="absolute">Elemento absolute</div>
</body>
</html>
```

---

## Flexbox

- `display: flex`: Activa el modo flexbox.
- `justify-content`: Alinea los elementos hijos horizontalmente.
- `align-items`: Alinea los elementos hijos verticalmente.
- `flex-direction`: Define la dirección de los elementos hijos (row, column).

---

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      display: flex;
      justify-content: space-around;
      align-items: center;
      height: 200px;
      background-color: lightgray;
    }
    .item {
      width: 100px;
      height: 100px;
      background-color: lightblue;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item">Item 3</div>
  </div>
</body>
</html>
```

---

## Grid

- `display: grid`: Activa el modo grid.
- `grid-template-columns`: Define las columnas de la cuadrícula.
- `grid-template-rows`: Define las filas de la cuadrícula.
- `gap`: Define el espacio entre los elementos de la cuadrícula.

---

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: 100px 100px;
      gap: 10px;
      background-color: lightgray;
    }
    .item {
      background-color: lightblue;
      padding: 20px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item">Item 3</div>
    <div class="item">Item 4</div>
    <div class="item">Item 5</div>
    <div class="item">Item 6</div>
  </div>
</body>
</html>
```
---

---

# Ejercicios HTML A

* Registrate en w3schools
* Completa ejercicios Tutorial: Learn HTML 106 ejercicios

---

# Introducción a JavaScript

---

## ¿Qué es JavaScript?

- JavaScript es un lenguaje de programación que permite crear contenido dinámico en las páginas web.
- Se ejecuta en el navegador del usuario.
- Interactúa con el HTML y el CSS para modificar el contenido y el estilo de una página web.

---

## Sintaxis Básica y Tipos de Datos

- Variables: `var`, `let`, `const`.
- Tipos de datos: `number`, `string`, `boolean`, `object`, `array`.
---
```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de JavaScript</title>
  <script>
    // Declaración de variables
    var numero = 42;
    let texto = "Hola, Mundo";
    const booleano = true;

    // Mostrar valores en la consola
    console.log(numero);
    console.log(texto);
    console.log(booleano);
  </script>
</head>
<body>
</body>
</html>
```
---

## Variables y Operadores

- Declaración de variables: `var`, `let`, `const`.
- Operadores: `+`, `-`, `*`, `/`, `%`, `++`, `--`.

---
```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Variables y Operadores</title>
  <script>
    // Declaración de variables
    let a = 10;
    let b = 20;

    // Operadores
    let suma = a + b;
    let resta = a - b;
    let multiplicacion = a * b;
    let division = a / b;

    // Mostrar resultados en la consola
    console.log("Suma: " + suma);
    console.log("Resta: " + resta);
    console.log("Multiplicación: " + multiplicacion);
    console.log("División: " + division);
  </script>
</head>
<body>
</body>
</html>
```

---

## Funciones y Eventos

- Funciones: Bloques de código reutilizables que realizan una tarea específica.
- Eventos: Acciones que ocurren en la página web (clics, movimientos del ratón, etc.).

---
```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Funciones y Eventos</title>
  <script>
    // Función que muestra un mensaje
    function mostrarMensaje() {
      alert("¡Hola, Mundo!");
    }
  </script>
</head>
<body>
  <button onclick="mostrarMensaje()">Haz clic aquí</button>
</body>
</html>
```

---

## Ejemplo, cambiar un texto
```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Script Simple</title>
  <script>
    // Función que cambia el contenido de un párrafo
    function cambiarContenido() {
      document.getElementById("miParrafo").innerHTML = "¡El contenido ha cambiado!";
    }
  </script>
</head>
<body>
  <p id="miParrafo">Este es un párrafo.</p>
  <button onclick="cambiarContenido()">Haz clic aquí</button>
</body>
</html>
```
---
# Manipulación del DOM con JavaScript

---

## ¿Qué es el DOM?

- DOM significa **Document Object Model**.
- Es una representación estructurada del documento HTML.
- Permite a JavaScript interactuar con y modificar el contenido y la estructura del documento.

---

## Selección de Elementos del DOM

- `document.getElementById(id)`: Selecciona un elemento por su ID.
- `document.getElementsByClassName(class)`: Selecciona elementos por su clase.
- `document.getElementsByTagName(tag)`: Selecciona elementos por su etiqueta.
- `document.querySelector(selector)`: Selecciona el primer elemento que coincide con el selector.
- `document.querySelectorAll(selector)`: Selecciona todos los elementos que coinciden con el selector.

---
```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Selección de Elementos del DOM</title>
  <script>
    window.onload = function() {
      // Selección por ID
      var elementoPorId = document.getElementById("miId");
      console.log(elementoPorId);

      // Selección por clase
      var elementosPorClase = document.getElementsByClassName("miClase");
      console.log(elementosPorClase);

      // Selección por etiqueta
      var elementosPorEtiqueta = document.getElementsByTagName("p");
      console.log(elementosPorEtiqueta);

      // Selección por selector
      var primerElemento = document.querySelector(".miClase");
      console.log(primerElemento);

      // Selección por todos los selectores
      var todosLosElementos = document.querySelectorAll(".miClase");
      console.log(todosLosElementos);
    };
  </script>
</head>
<body>
  <p id="miId">Elemento con ID</p>
  <p class="miClase">Elemento con clase</p>
  <p class="miClase">Otro elemento con clase</p>
</body>
</html>
```
---

## Modificación de Contenido y Estilos

- `element.innerHTML`: Modifica el contenido HTML de un elemento.
- `element.style.property`: Modifica el estilo de un elemento.
---

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Modificación de Contenido y Estilos</title>
  <script>
    function modificarContenido() {
      var elemento = document.getElementById("miParrafo");
      elemento.innerHTML = "El contenido ha sido modificado.";
      elemento.style.color = "red";
      elemento.style.fontSize = "20px";
    }
  </script>
</head>
<body>
  <p id="miParrafo">Este es un párrafo.</p>
  <button onclick="modificarContenido()">Modificar Contenido</button>
</body>
</html>
```

---

## Creación y Eliminación de Elementos

- `document.createElement(tag)`: Crea un nuevo elemento.
- `parentElement.appendChild(childElement)`: Añade un elemento hijo a un elemento padre.
- `parentElement.removeChild(childElement)`: Elimina un elemento hijo de un elemento padre.

---
```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Creación y Eliminación de Elementos</title>
  <script>
    function crearElemento() {
      var nuevoElemento = document.createElement("p");
      nuevoElemento.innerHTML = "Este es un nuevo párrafo.";
      document.body.appendChild(nuevoElemento);
    }

    function eliminarElemento() {
      var elemento = document.getElementById("miParrafo");
      elemento.parentNode.removeChild(elemento);
    }
  </script>
</head>
<body>
  <p id="miParrafo">Este es un párrafo que será eliminado.</p>
  <button onclick="crearElemento()">Crear Elemento</button>
  <button onclick="eliminarElemento()">Eliminar Elemento</button>
</body>
</html>
```
---

# Introducción a Bootstrap

---


## ¿Qué es Bootstrap?

- Bootstrap es un framework de CSS que facilita la creación de sitios web responsivos y modernos.
- Incluye una colección de herramientas de diseño, como un sistema de grid, componentes predefinidos y plugins de JavaScript.

---

## Instalación y Configuración

- Puedes incluir Bootstrap en tu proyecto de dos maneras:
  - **CDN**: Añadiendo un enlace a los archivos de Bootstrap alojados en un servidor.
  - **Descarga**: Descargando los archivos de Bootstrap y añadiéndolos a tu proyecto.

```html
<!-- Ejemplo de instalación vía CDN -->
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
```
---

## Sistema de Grid de Bootstrap

- El sistema de grid de Bootstrap utiliza una serie de contenedores, filas y columnas para diseñar y alinear contenido.
- Las clases principales son `.container`, `.row`, y `.col`.

```html
<!-- Ejemplo del sistema de grid -->
<div class="container">
  <div class="row">
    <div class="col">
      Columna 1
    </div>
    <div class="col">
      Columna 2
    </div>
  </div>
</div>
```

---

## Componentes Básicos

- Bootstrap incluye una variedad de componentes predefinidos, como botones, tarjetas y menús de navegación.
- Estos componentes se estilizan utilizando clases específicas de Bootstrap.

```html
<!-- Ejemplo de un botón -->
<button type="button" class="btn btn-primary">Botón Primario</button>
```
---
## Ejemplo completo

```html
<!-- Ejemplo de página con Bootstrap -->
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
  <title>Página con Bootstrap</title>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        Columna 1
      </div>
      <div class="col">
        Columna 2
      </div>
    </div>
    <button type="button" class="btn btn-primary mt-3">Botón Primario</button>
  </div>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```
