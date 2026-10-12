# Descripción del Funcionamiento de los Archivos en un Servidor Web

## Archivos Involucrados
- **`get.html`**: Página HTML que permite interactuar con los datos.
- **`data.json`**: Archivo JSON que contiene los datos disponibles.

## Descripción del Proceso
El archivo `get.html` es una página HTML que permite al usuario interactuar con un archivo JSON llamado `data.json` mediante el método HTTP GET. La página tiene un campo de entrada y un botón que, al ser presionado, envía una solicitud GET para obtener información del archivo `data.json` utilizando JavaScript.

El archivo `data.json` contiene una serie de objetos con campos `id`, `title` y `body`. Cada objeto representa un conjunto de datos que se puede consultar.

### Paso a Paso del Proceso

1. **Interfaz de Usuario (`get.html`)**:
   - El usuario introduce un `ID` en un campo de entrada.
   - Al hacer clic en el botón "Obtener Datos", se dispara un evento que envía una solicitud GET al archivo `data.json`.

2. **Solicitud y Procesamiento de Datos (`get.html`)**:
   - Se usa `XMLHttpRequest` para hacer una solicitud GET a `data.json` pasando el parámetro `id`.
   - La respuesta es analizada y se busca un objeto que coincida con el `ID` proporcionado por el usuario.
   - Si se encuentra, la información se muestra en la página (`<pre id="result">`).
   - Si no se encuentra, se muestra un mensaje indicando que no hay datos para ese `ID`.

### Uso en un Servidor Web
En un servidor web, estos archivos serían usados para simular la obtención de datos locales sin necesidad de una API o base de datos, lo cual es útil para pruebas o demostraciones de cómo funciona el método GET en aplicaciones web.

## Ejemplo del Código JavaScript Utilizado (`get.html`)
```html
<script>
    document.getElementById('fetchData').addEventListener('click', function() {
        const id = document.getElementById('idInput').value;
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `data.json?id=${id}`, true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                const result = data.find(item => item.id == id);
                if (result) {
                    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
                } else {
                    document.getElementById('result').innerText = 'No se encontraron datos para el ID proporcionado.';
                }
            } else {
                console.error('Error al obtener los datos:', xhr.statusText);
            }
        };
        xhr.onerror = function() {
            console.error('Error de red');
        };
        xhr.send();
    });
</script>
```
