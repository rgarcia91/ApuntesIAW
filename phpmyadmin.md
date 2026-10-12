# Introducción

La aplicación tan sólo es un conjunto de archivos escritos en PHP que se copian en un directorio del servidor web, de forma que, cuando se accede a estos archivos, encontramos una herramienta que nos permite crear tablas, insertar datos en las tablas existentes, navegar por los registros de las tablas, editar y borrar, borrar tablas, etc. Incluso ejecutar sentencias SQL y hacer una copia de seguridad de la base de datos.

# Instalación del phpMyAdmin

## Instalación desde el código o mediante un paquete de distribución

  La página de inicio del proyecto es www.phpmyadmin.net. Desde aquí podéis bajar los ficheros de la última versión de la aplicación, que después tenéis que colocar en nuestro servidor web.

Para distribuciones GNU/Linux basadas en Debian, también se puede hacer la instalación directamente desde el repositorio:

```# sudo apt-get install phpmyadmin```

Durante la instalación os hará una serie de preguntas:

•  En cuanto al servidor web que usará tenéis que contestar: apache2.
•  Cuando os pregunta si queréis configurar la base de datos phpMyAdmin con
*dbconfig-common*, tenéis que contestar que sí.
•  Cuando os pregunta la contraseña de root de MySQL (porque phpMyAdmin
quiere crear sus tablas a la base de datos MySQL)
•  Os pedirá la clave de acceso a la base de datos MySQL del usuario que se ha
creado por el phpMyAdmin. Podéis escribir una clave vosotros o, si la dejáis en
blanco, creará una clave aleatoria.

**Antes de poder acceder al panel de control de phpMyAdmin** se tiene que modificar la configuración de Apache.

Buscáis donde está el fichero **apache.conf**. Generalmente lo tendríais que tener a **/etc/phpmyadmin/apache.conf**

En cualquier caso lo podéis encontrar con las órdenes:

**#updatedb**

**#locate apache.conf**

**Editáis** la **configuración de Apache** **e incluid el fichero apache.conf de phpMyAdmin.**

Por eso abrís (con derechos de root ) el fichero **/etc/apache2/apache2.conf** y añadís al final del fichero la siguiente línea:

***Include /etc/phpmyadmin/apache.conf***

Ahora ya podéis reinicar el servidor Apache e ir a la dirección http://localhost/phpmyadmin para ver si funciona. Tendríais que encontrar una pantalla como la que se puede ver a la figura 1.8.

![](img/Aspose.Words.c06e9a43-1e65-4df2-82f7-abe4447d36d6.008.png)

## Instalación en un contenedor docker

Teniendo docker ya instalado tenemos una imagen oficial donde
sólo debemos ejecutar un contenedor con mysql y luego ejecutar el phpmyadmin

Ejemplo

```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.31-debian
docker run --name myadmin -d --link some-mysql:db -p 8080:80 phpmyadmin
```
Comprobaremos su conexion en localhost:8080 Usuario root y password my-secret-pw

## Gestión de la interfaz de phpmyadmin

Si se accede con un usuario que sea administrador de MySQL, el phpMyAdmin permite gestionar todas las bases de datos existentes del servidor. De otro modo, sólo se muestran las bases de datos a las que se tiene acceso. Los usuarios administradores tienen acceso a una base de datos llamada mysql (base de datos de control) que sirve para configurar el motor de bases de datos. Es muy importante no tocarla ni hacer cambios a menos que se sepa perfectamente lo que está haciendo. En caso contrario, el MySQL podría dejar de funcionar o quedar inoperativo.

Para acceder a ella hay que entrar desde el navegador a la dirección <http://localhost/phpmyadmin>.

Una vez introducidos los datos de acceso (nombre y contraseña) debe ver una pantalla como la de la figura1.

Figura Pantalla inicial de PHPMyAdmin

![](img/Aspose.Words.5c8def73-1a0a-4746-803a-c87514a0ec49.001.png)

El phpMyAdmin divide la ventana en dos marcos. El de la izquierda ofrece un menú desplegable con las bases de datos a las que se tiene acceso (si son más de una) y las tablas de la base de datos seleccionada. El marco de la derecha es el lugar en el que se muestra la información de la navegación. Inicialmente muestra una pantalla de bienvenida con varios enlaces.

Al hacer clic en el nombre de las tablas que se muestran en el marco de la izquierda se puede ver la estructura (los campos) en el marco de la derecha y aparece un menú horizontal que permite acceder a las diversas funcionalidades del aplicación.

Si selecciona una base de datos existente (por ejemplo mysql) verá por defecto un listado de todas las tablas que existen en la base de datos, tal como se puede ver en la figura.2.

Figura 2. Vista de base de datos

![](img/Aspose.Words.5c8def73-1a0a-4746-803a-c87514a0ec49.002.png)

Si hace clic en cualquiera de las tablas, puede ver la estructura de la tabla, examinar su registros o insertar uno nuevo.

Haciendo clic en la pestaña SQL puede insertar consultas directamente utilizando sintaxis SQL. Esto es muy útil cuando está programando, ya que puede comprobar si las consultas que está realizando durante el programa son correctas o no. Simplemente copie el texto de la consulta en la caja y haga clic en Continuar. Puede ver los registros resultantes de la consulta que ha hecho.

Finalmente, con la opción Exportar puede extraer los datos de la base de datos a un archivo de texto plano que puede importar posteriormente, con la opción Importar, a una base de datos MySQL.
