# Programación web de servidor Acceso a bases de datos desde PHP

**Índice**

1. [Gestores de bases de datos más usados](#1-gestores-de-bases-de-datos-más-usados)
2. [Gestión de bases de datos](#2-gestión-de-bases-de-datos)
    1. [2.1 Mysql Client](#21-mysql-cliente)
    2. [2.2 PhpMyAdmin](#22-phpmyadmin)
3. [Conexión con el servidor MySQL](#3-conexión-con-el-servidor-mysql)
4. [Cerrar la conexión a la base de datos](#4-cerrar-la-conexión-a-la-base-de-datos)
5. [Selección de la base de datos](#5-selección-de-la-base-de-datos)
6. [Trabajo con la base de datos](#6-trabajo-con-la-base-de-datos)
   1. [6.1 Inserción de información](#61-inserción-de-información)
   2. [6.2 Consulta de información](#62-consulta-de-información)
   3. [6.3 Modificación de información](#63-modificación-de-información)
7. [Creación de una base de datos](#7-creación-de-una-base-de-datos)
    1. [7.1 Creación de tablas](#71-creación-de-tablas)
8. [Mecanismos de seguridad	](#8-mecanismos-de-seguridad)
    1. [8.1 Codificación de la información](#81-codificación-de-la-información)

El mayor beneficio de trabajar con páginas dinámicas es que puede tomar la información que se mostrará de una base de datos, en lugar de tener que tenerla dentro del código o en un fichero externo. El uso de MySQL con PHP es muy popular en el desarrollo de aplicaciones web.

# 1. Gestores de bases de datos más usados

Existen diferentes bases de datos en el mercado que puede utilizar para crear su página web con bases de datos. Es importante conocer las más populares para poder decidir en cada caso cuál será la óptima para vosotros.

- **MySQL:** es una plataforma gratuita y muy adecuada para aprender. Es posiblemente una de las bases de datos más rápidas que podemos encontrar, además de consumir pocos recursos de la máquina donde está instalada. Se trata de un sistema relativamente fácil de instalar y administrar frente a otros productos del mercado. Se recomienda para iniciarse en el mundo de las bases de datos, ya que dispone de muchas utilidades, manuales y documentación que la inmensa comunidad de usuarios ha encargado de realizar desinteresadamente. La gestión de la base de datos utiliza el SQL (Structured Query Language), además de utilizar protocolos de comunicación de bases de datos desarrolladas por Microsoft, mediante ODBC o ADO.

ORDBMS (Object-Relational Database Management System, sistema de gestión de bases de datos objeto-relacionales) es un sistema gestor de bases de datos similar a los relacionales, pero con un modelo de bases de datos objeto-relacionales con objetos, clases y herencia.

- **PostgreSQL:** es un gestor de bases de datos usado principalmente para grandes organizaciones en aplicaciones críticas o importantes. PostgreSQL es la segunda base de datos más popular implantada en el mercado GNU / Linux. PostgreSQL se diseñó como una base de datos orientada a objetos, es decir, una ORDBMS, con la que el concepto de tablas lo sustituimos por objetos, y se permite crear nuevos tipos de datos, hacer herencias entre objetos, etc. PostgreSQL es, sin duda, una de las bases de datos que ha aportado más implementaciones para los expertos. Dispone de lo que a MySQL le falta, pero también le falta todo lo que el MySQL tiene. PostgreSQL tiene transacciones, integridad referencial, vistas y un gran número de funcionalidades, a cambio de convertirse en un motor más lento y pesado que MySQL.

- **Oracle:** es uno de los sistemas de gestión de bases de datos relacional más importantes. Está disponible en una variedad de configuraciones, desde pequeñas versiones personales hasta versiones empresariales.

- **Microsoft Access:** es un sistema de pago que permite realizar un diseño de la base de datos mediante una herramienta gráfica. Tiene ciertas limitaciones importantes (como el número de conexiones concurrentes que puede tratar) y hay pocos sistemas operativos sobre los que puede funcionar.

- **Microsoft SQL Server:** está diseñado para crear webs y sistemas de bases de datos empresariales de escritorio. Permite almacenar grandes cantidades de información comparado con Access.

Utilizaremos MySQL porque: es ideal para aplicaciones pequeñas, aunque al ser escalable también se puede utilizar para aplicaciones grandes; es muy rápido, confiable y fácil de usar; utiliza SQL estándar; compila una gran cantidad de plataformas; y, finalmente, porque es gratuito de descargar y usar.

# 2. Gestión de bases de datos

## 2.1 mysql cliente

Es un programa cliente que ejecutamos en el terminal para poder gestionar operaciones sobre la base de datos 

[Comandos mysql](climysql.md)

## 2.2 Phpmyadmin

Es una herramienta libre y gratuita escrita en PHP que permite controlar la administración de MySQL desde un navegador web. Permite realizar diferentes tareas tales como crear, modificar o borrar bases de datos, tablas, campos o filas ... ejecutando órdenes SQL.

[phpmyadmin](phpmyadmin.md)

# 3. Conexión con el servidor MySQL

La estructura para acceder a una base de datos es muy similar al protocolo para acceder a un archivo:

1. Abrir la base de datos.
1. Enviar el pedido SQL en la base de datos.
1. Devolver el resultado de la consulta.
1. Cerrar la conexión de la base de datos.

Antes de poder acceder a los datos en una base de datos, se debe crear una conexión con la base de datos. En PHP para conectar con la base de datos MySQL esto se hace con la función **$conn = mysqli_connect();**

**$conn = mysqli_connect(nombre del servidor, nombre de usuario, contraseña);**


La función **mysqli_connect** devuelve una conexión con el servidor MySQL Server en caso de éxito, o FALSE y un error en caso de fallo. Puede ocultar la salida de error mediante la adición de una @ delante del nombre de la función.

Esta es la descripción de los parámetros:

- Nombre del servidor: es opcional. Especifica el servidor MySQL al que conectar. Puede incluir un número de puerto, por ejemplo Servidor: puerto o una ruta, por ejemplo,*: /camino/al/directorio* para el localhost. Si la directiva de PHP *mysql.default\_host* no está definida (por defecto), entonces el valor por defecto es *localhost: 3306*. En el modo SQL seguro, este parámetro se ignora y *localhost: 3306* se utiliza siempre.

- Nombre de usuario: es opcional. Especifica el nombre de usuario para iniciar la sesión. El valor por defecto es el nombre del usuario propietario del proceso del servidor que está definido por la directiva *mysql.default\_user*. En el modo SQL seguro, este parámetro se ignora y se usa el nombre del usuario propietario del proceso del servidor.

- Contraseña: es opcional. Especifica la contraseña para iniciar sesión. El valor predeterminado es definido por la directiva *mysql.default\_password*. En el modo SQL seguro, este parámetro no se tiene en cuenta y se usa la contraseña vacía.

En el siguiente ejemplo se almacena la conexión en una variable ($conexion) para su uso posterior. Si la conexión falla ejecutará el código dentro del *if* y el programa saldrá.

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?> 
```

# 4. Cerrar la conexión a la base de datos

La función de PHP **mysqli_close();**, cierra una conexión MySQL. Esta función devuelve TRUE si tiene éxito, o FALSE en caso de fallo.

Tiene un único argumento opcional que es la conexión MySQL para cerrar. Si no se especifica, se utiliza la última conexión abierta por **mysqli_close();**

El uso de **mysqli_close();** no es imprescindible, ya que las conexiones no persistentes son cerradas automáticamente al final de la ejecución del script PHP.

Este es un ejemplo de utilización:

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";

mysqli_close($conn); 
echo "Conexión cerrada";

?>
```

# 5. Selección de la base de datos

Antes de empezar a trabajar con una base de datos del servidor, debemos seleccionar. Para ello, existe la función **mysqli_select_db($conexion, $nombre);** que toma dos argumentos que especifican la conexión al servidor que hemos hecho con anterioridad y el nombre de la base de datos que queremos escoger, respectivamente. La función devuelve TRUE en caso de éxito, y FALSE en caso de error.

He aquí un ejemplo de utilización de la función:

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";

mysqli_select_db($con, "test");
?>
```

# 6. Trabajo con la base de datos

Con una base de datos se pueden hacer varias operaciones: **consultar datos, insertar datos, actualizar datos y borrar datos.**

Para estas operaciones la estructura del código de programación es exactamente igual. Siempre que se programa una conexión a una base de datos MySQL se realizarán los siguientes pasos:

1. Conexión al servidor MySQL: para hacer esta operación se utiliza la función **$conn = mysqli_connect(nombre del servidor, nombre de usuario, contraseña);**. La función devuelve un valor del tipo *resource (recurso)*, que representa la conexión con la base de datos.

1. Selección de la base de datos con la que se trabaja: con **mysqli_select_db($conexion, $nombre);**. Se debe indicar la conexión con el servidor y el nombre de la base de datos con la que se quiere trabajar.

1. Hacer la consulta/operación necesaria con la función **$result = mysqli_query($conexion, $consulta);**

4. Puede comprobar cuántas filas ha devuelto un SELECT o han sido insertadas modificadas. Para consultar cuántas filas ha devuelto un consulta, puede utilizar la función **mysqli_num_rows($result)** que devuelve el número de filas que se han seleccionado con un **SELECT o SHOW**. Para consultar cuántas filas han sido insertadas, modificadas o borradas con INSERT, UPDATE, REPLACE o DELETE, puede utilizar la función **mysqli_affected_rows($con);**

4. Si es una operación de consulta de datos (como un SELECT), falta leer los datos que devuelve la consulta SQL. Para ello puede utilizar la función **$row = mysqli_fetch_assoc($result)** que devuelve los valores en forma de matriz asociativa en la que las claves son las columnas de la tabla. Devuelve FALSE si no hay más filas.

## 6.1 Inserción de información

Para añadir registros en la base de datos debe utilizar una consulta MySQL de tipo INSERT que tiene la siguiente estructura:

**INSERT INTO nom\_taula [(columna1, columna2, ...)] VALUES (valor1, valor2,...);**

Puede consultar la sintaxis completa en: <http://dev.mysql.com/doc/refman/5.5/en/insert.html>

Por ejemplo:

"INSERT INTO discos(titulo, autor, any) VALUES ('Axis: Bold as love', 'The Jimi Hendrix Experience', '1967')";

El siguiente ejemplo muestra un código entero de inserción de datos en una base de datos:

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', 'john@example.com')";

if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?> 
```
Puede comprobar posteriormente que se ha insertado los datos (con una consulta MySQL o desde PHPMyAdmin, por ejemplo).

La gracia de las páginas dinámicas es que la información que se ha de insertar en la base de datos no es estática, como en este ejemplo, sino que son valores que introducen los usuarios. Esta tarea se hace mediante el uso de formularios. La secuencia de acciones es la siguiente:

1. El usuario introduce datos con un formulario.
1. Cuando valida el formulario con el botón, se envían los datos utilizando el método POST o GET.
1. Recibidos los datos del formulario se hace la conexión a la base de datos y la inserción de los datos.

## 6.2 Consulta de información

Para realizar una consulta en la base de datos para obtener información, debe utilizar una sentencia SELECT, que tiene la siguiente forma:

```
SELECT
expressió
FROM taula
WHERE condició
[GROUP BY {columna | expressió | posició}
[ASC | DESC]]
[HAVING condició]
[ORDER BY {columna | expressió | posició}
[ASC | DESC]]
[LIMIT {[desplaçament,] num\_files | num\_files OFFSET offset}]
```
Puede consultar la sintaxis completa en:

<http://dev.mysql.com/doc/refman/5.6/en/select.html>

Por ejemplo:

SELECT nom, dni FROM usuaris WHERE uid=1

Una vez creada la consulta y almacenada en una variable, puede ejecutarla en base de datos con la función **$result = mysqli_query(conexion, consulta);**

Esta función:

- Para consultas del tipo SELECT, SHOW, Describe, Explain devuelve una variable de tipo *resource(recurso)* en caso de éxito y FALSE en caso de error.
- Para consultas INSERT, UPDATE, DELETE, DROP, retorna TRUE en caso de éxito y FALSE en caso de error.

Una vez que haya hecho la consulta SELECT, puede averiguar cuántas filas ha devuelto la consulta con la función **int mysqli_num_rows($resultado)** que devuelve el número de filas que ha devuelto el SELECT o FALSE en caso de error.

Para obtener los datos del resultado de la consulta utiliza la función **$row = mysqli_fetch_assoc($result)** que devuelve un array asociativo que corresponde a una fila del resultado de la consulta (y avanza el puntero que indica la fila a mostrar).

La función devolviendo las diferente filas resultantes del SELECT según como es llamada, hasta que llega a la última fila resultante, en la que devuelve FALSE. Por lo tanto, para obtener todos los datos de retorno de un SELECT, debe llamar a **$row = mysqli_fetch_array($resultado, $tipo);** dentro de un bucle hasta que la función le devuelva FALSE. Por ejemplo:

El argumento $ tipo indica el tipo del array asociativo que se obtiene. Es una constante que puede coger los siguientes valores: MYSQL\_ASSOC, MYSQL\_NUM o MYSQL\_BOTH (que es el valor por defecto). Si deja este parámetro en blanco o seleccione MYSQL\_BOTH obtendrá un array con el que puede acceder a los elementos tanto por número de la columna, como por su nombre.



``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT id, firstname, lastname FROM MyGuests";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
  // output data of each row
  while($row = mysqli_fetch_assoc($result)) {
    echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
  }
} else {
  echo "0 results";
}

mysqli_close($conn);
?>
```

## 6.3 Modificación de información

Para codificar la información de la base de datos debe utilizar la consulta UPDATE de MySQL que tiene la siguiente forma:

```
UPDATE taula
SET nomColumna1={expressió1|DEFAULT},
nomColumna2={expressió2|DEFAULT}...
WHERE condició
[LIMIT numero\_files]
```

Puede ver la sintaxis completa a:

<http://dev.mysql.com/doc/refman/5.6/en/update.html>

Por ejemplo:
UPDATE taula SET id='200' WHERE id=2;
o
UPDATE taula1 SET col1 = col1 + 1, col2 = col1;

No hay que poner las comillas a la condición WHERE.

La utilizará mediante la función **$result = mysqli_query(conexion, consulta);**
. Posteriormente puede utilizar la función **mysqli_affected_rows($con);** para obtener la cantidad de filas modificadas con la sentencia.

En el siguiente ejemplo se modifican los datos en una base de datos en función de los valores enviados por un formulario HTML.

//Connexión con la base de dades i selección base de datos

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "UPDATE MyGuests SET lastname='Doe' WHERE id=2";

if (mysqli_query($conn, $sql)) {
  echo "Record updated successfully";
} else {
  echo "Error updating record: " . mysqli_error($conn);
}

mysqli_close($conn);
?> 
```



**6.4 Borrar registros**

Para borrar registros de una tabla debe utilizar una consulta DELETE que tiene la siguiente forma:

```
DELETE FROM taula
[WHERE condició]
[ORDER BY ...]
[LIMIT numero\_files]
```
Puede encontrar la sintaxis entera en:

<http://dev.mysql.com/doc/refman/5.6/en/delete.html>

Por ejemplo:

DELETE FROM taula WHERE id < 10

La utilizará mediante la función mysql\_query ($ consulta). Posteriormente podemos utilizar la función mysql\_affected\_rows () para obtener la cantidad de filas modificadas con la sentencia.

En el siguiente ejemplo se borra un elemento :
La utilizará mediante la función **$result = mysqli_query(conexion, consulta);**
Posteriormente puede utilizar la función **mysqli_affected_rows($con);** para obtener la cantidad de filas modificadas con la sentencia.

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// sql to delete a record
$sql = "DELETE FROM MyGuests WHERE id=3";

if (mysqli_query($conn, $sql)) {
  echo "Record deleted successfully";
} else {
  echo "Error deleting record: " . mysqli_error($conn);
}

mysqli_close($conn);
?> 
```
La función *mysqli_connect_error()* devuelve un texto con la descripción del error de la última función MySQL que se ha ejecutado. Por tanto, la debe ejecutar justamente después de la función de la cual desea saber el error.

En el caso de que no haya ningún error, devuelve una cadena vacía ("").


# 7. Creación de una base de datos

Hay varias formas de crear una base de datos. Generalmente la creaban con una herramienta como puede ser en terminal mysql o via web con PHPMyAdmin, aunque lo puede hacer también desde el código.

Para crear una base de datos en MySQL se utiliza la sentencia:

mysql> CREATE DATABASE Nom\_base\_de\_dades;

En ambientes Unix, los nombres de las bases de datos son case sensitive (al contrario que las palabras clave), por lo que siempre debe referirse a la base de datos exactamente igual (y no *nom\_base\_de\_dades o NOM\_BASE\_DE\_DADES*). Esto también se aplica a los nombres de tablas. Esta restricción no existe en Windows, aunque puede utilizar el mismo esquema de mayúsculas cuando se refiera a bases de datos y tablas en una consulta dada.

El pedido mysqli_query($conn, $sql) de PHP envía una sentencia en la base de datos. Por lo tanto puede utilizarla para crear una base de datos en el servidor:

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = mysqli_connect($servername, $username, $password);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Create database
$sql = "CREATE DATABASE myDB";
if (mysqli_query($conn, $sql)) {
  echo "Database created successfully";
} else {
  echo "Error creating database: " . mysqli_error($conn);
}

mysqli_close($conn);
?>

```
Al crear una base de datos, ésta no se selecciona para su uso automáticamente, se debe hacer explícitamente. La sintaxis para hacerlo a MySQL es

mysql> USE Nom\_base\_de\_dades

Las bases de datos sólo necesitan ser creadas una sola vez, pero deben ser seleccionadas cada vez que se inicia una sesión de MySQL. Se puede hacer a través del pedido USE como se muestra en el ejemplo. Cuando acceda a MySQL desde consola lo puede indicar en la línea de comandos al ejecutar MySQL. Simplemente se debe indicar el nombre de la base de datos después de los parámetros que necesita para ingresar. Por ejemplo:

**shell> mysql -h host -o user -p LaMevaBD**

Adviértase que en el comando anterior LaMevaBD no es la contraseña. Si se quisiera suministrar la contraseña en la línea de comandos, después de la opción -p, debe hacerse sin dejar espacios en blanco (por ejemplo, -pcontrasenya, no -p contraseña). De todas formas, escribir la contraseña en la línea de comandos no es recomendable porque lo expone a la vista de otros usuarios.

Para eliminar una base de datos en PHP, al igual que para la creación de una base de datos, utilizará el comando **mysqli_query($conn, $sql)** para ejecutar la instrucción DROP DATABASE, tal como se puede ver en el siguiente ejemplo:
``` php
<?php
    $sql = 'DROP DATABASE LaMevaBD';
    mysqli_query($conn, $sql)
?>
```
Puede ver el contenido de las tablas con el orden de MySQL SHOW TABLES directamente sobre MySQL:

mysql> SHOW TABLES;
Empty septiembre (0.00 sec)

En un principio la base de datos recién creada está vacía.

## 7.1 Creación de tablas

En MySQL puede utilizar la sentencia CREATE TABLE para especificar la estructura de una tabla:

CREATE TABLE nombre\_tabla
(
nom\_columna1 tipus\_dades,
nom\_columna2 tipus\_dades,
nom\_columna3 tipus\_dades,
)

Siempre que desea ejecutar órdenes al MySQL puede utilizar la función de PHP mysqli_query($conn, $sql). En este caso se debe ejecutar la instrucción de MySQL CREATE TABLE, como se puede ver en el siguiente ejemplo:

``` php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// sql to create table
$sql = "CREATE TABLE MyGuests (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";

if (mysqli_query($conn, $sql)) {
  echo "Table MyGuests created successfully";
} else {
  echo "Error creating table: " . mysqli_error($conn);
}

mysqli_close($conn);
?>
```
Después de crear la tabla , desde MySQL con el comando SHOW TABLES debería producir la siguiente salida :

mysql> SHOW TABLES;

| Tables in LaMevaBD |
| ------------------ |
| nom\_taula |

Para verificar que la tabla ha sido creada en la forma esperada , utilice la sentencia Describe a MySQL :

mysql> DESCRIBE nom\_taula;


| Field | Type | Null | Key | Default | Extra |
| ----- | ----- | ---- | -- | -------- | ---- |
| col1  | tipus | ca    |        | NULL    |          |
| col2  | tipus | ca    |        | NULL    |          |
| col3  | tipus | ca    |        | NULL    |          |


La sentencia  *DESCRIBE*  puede ser utilizada en cualquier momento, por ejemplo, si olvida los nombres o el tipo de datos de las columnas de la tabla.

# 8. Mecanismos de seguridad

La seguridad es un tema complejo que requiere una planificación a todos los niveles en que se está trabajando la página web y la base de datos. Por un lado usted utilizará contraseñas que lo más adecuado es que guarde de forma encriptada en la base de datos.

Los usuarios únicamente deben poder acceder a las páginas de la web a las que tienen permisos. Por ejemplo, un usuario alumno del no tiene acceso a la edición del aula.

Por otra parte, los usuarios de la base de datos, deben tener únicamente la capacidad de acceder a los datos estrictamente necesarios. Los usuarios dentro de la base de datos también tienen un acceso limitado a ella.

## 8.1 Codificación de la información

Puede utilizar el algoritmo MD5 para codificar los datos confidenciales dentro de la base de datos. Puede encontrar la especificación aquí:

[*www.faqs.org/rfcs/rfc1321.html*](http://www.faqs.org/rfcs/rfc1321.html)

Afortunadamente MD5 está implementado directamente en PHP, por eso puede calcular el MD5 de una cadena simplemente llamando a una función.

La función string *md5($cadena)* encripta la cadena utilizando el algoritmo MD5 y la devuelve en forma de número hexadecimal de 32 caracteres.

El uso del algoritmo SHA1 o MD5 no es estrictamente seguro para almacenar los datos, tal como se puede ver en este artículo de PHP.net [www.php.net/manual/en/faq.passwords.php#faq.passwords .fasthash](http://www.php.net/manual/en/faq.passwords.php#faq.passwords%20.fasthash), pero para hacer nuestras pruebas tendrá una seguridad suficiente y servirá para aprender a trabajar con claves encriptadas.

El siguiente es un ejemplo muy sencillo en el que se ve el funcionamiento de la función:
[md5](http://www.php.net/md5)

``` php
<?php
$str = 'apple';

if (md5($str) === '1f3870be274f6c49b3e31a0c6728957f')
{
echo "Tens un ordinador Apple";
}
?>
```

En el siguiente ejemplo se ve cómo crear una consulta donde se comprueba si el valor de nombre y contraseña obtenido de un formulario está en la base de datos :
```
$consulta = sprintf('select from usuaris where nom="%s" and passwd = "%s"', $_POST["nom"], $_POST["passwd"]);
```
En caso de que las llaves estuvieran encriptados en la base de datos, se podría crear la consulta así :
```
$consulta = sprintf('select  from usuaris where nom="%s" and passwd = "%s"', $_POST["nom"], md5(($_POST["passwd"]));
```
La función *sprintf( ) de PHP funciona de forma similar a la versión de C. Es como un *printf*, pero en lugar muestra el resultado por pantalla, lo devuelve a un string . Os puede resultar muy útil para crear consultas. Puede ver aquí la especificación completa de la función :

[*www.php.net/manual/en/function.sprintf.php*](http://www.php.net/manual/en/function.sprintf.php)

En este caso , recuerde que al crear un usuario , su clave también deberá estar encriptada. por ejemplo

``` php
$consulta = sprintf('INSERT into usuaris (nom, passwd, administrador) VALUES ("%s","%s","%s");
```

Una característica muy habitual de las webs actualmente es la de presentar diferentes contenidos de la web dependiendo de cuál sea el perfil del usuario. También hay ciertas páginas que pueden estar protegidas para impedir el acceso a los usuarios que no tienen los privilegios necesarios.

Por ejemplo, un usuario que no está registrado en www.amazon.com puede navegar y ver los productos que están a la venta . Pero no podrá realizar compras a menos que esté registrado, y que haya iniciado una sesión. De igual manera, un usuario registrado no podrá acceder a las páginas de administración de la web si no tiene los permisos necesarios.

Para implementar estos permisos de acceso puede utilizar sesiones o almacenar en la base de datos la estructura de páginas de la web y qué usuarios tienen acceso .

