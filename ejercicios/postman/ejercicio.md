# Ejemplos Básicos de Uso de Postman

## Instalación de Postman
- Descarga e instala Postman desde su sitio oficial.

## Crear una Colección
- Una colección es un grupo de solicitudes relacionadas. Para crear una, haz clic en el botón **"New"** y selecciona **"Collection"**. Dale un nombre y guarda.

## Agregar una Solicitud
- Dentro de tu colección, puedes agregar solicitudes. Haz clic en **"New"** y selecciona **"Request"**. Elige el tipo de solicitud (GET, POST, PUT, DELETE) y configura la URL de la API.

## Configurar la Solicitud
- Especifica los parámetros y encabezados necesarios en las pestañas **"Params"** y **"Headers"**. Por ejemplo, si estás haciendo una solicitud GET a `https://api.ejemplo.com/users`, puedes agregar parámetros como `id=1`.

## Enviar la Solicitud
- Una vez configurada, haz clic en **"Send"**. Postman mostrará la respuesta de la API, incluyendo el código de estado, encabezados y cuerpo de la respuesta.

## Pruebas Automatizadas
- Postman permite definir pruebas automatizadas que se ejecutan después de enviar la solicitud. Puedes escribir scripts en la pestaña **"Tests"** para verificar que la respuesta sea la esperada.

## Ejemplo Práctico

### Solicitud GET
- **URL**: `https://jsonplaceholder.typicode.com/posts/1`
- **Método**: GET
- **Parámetros**: Ninguno
- **Encabezados**: Ninguno

### Solicitud POST
- **URL**: `https://jsonplaceholder.typicode.com/posts`
- **Método**: POST
- **Cuerpo (Body)**:
  ```json
  {
    "title": "foo",
    "body": "bar",
    "userId": 1
  }
   ```
- **Encabezado**: `Content-Type: application/json`