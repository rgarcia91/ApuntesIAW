# Mysql Client

0. [Introduccion](#introduccion)
1. [Seguridad en la base de datos](#seguridad-en-la-base-de-datos)
2. [Verificación y pruebas](#verificación-y-pruebas)
    1. [Nagios](#nagios)
    2. [Pandora FMS](#nagios)
    3. [Pruebas de rendimiento](#pruebas-de-rendimiento)

# Introduccion

Hay un programa llamado igual que la base de datos mysql que hace de cliente para conectarnos al sistema gestor de base de datos mysql servidor.
Es la forma mas sencilla de gestionar la base de datos

En un terminal escribiréis la petición siguiente:

```
$ sudo mysql -h localhost -u root -p
```

**Enter password:**
```
Welcome tono the MySQL monitor. Commands end with ;
Your MySQL connection id is XX
Server version: 5.1.49 3 (Debian)
Copyright (c) 2000, 2010, Oráculo  its affiliates. Ajo rights reserved.
This software comas with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome tono modify and redistribute it under the GPL v2 license

Type help  or h for help. Type c to clear the current input statement.
```
```mysql> show databases;```

| Database |
| -- |
| information_schema |
| mysql | 
| rows in siete (0.00 seco) |
| mysql> quit |
| Bye |

## Seguridad en la base de datos

Las listas de control de acceso (ACL en inglés Access Control List) son el mecanismo de seguridad que utiliza MySQL para todas las conexiones y consultas que los usuarios pueden intentar realizar. Una lista de control de acceso controla si un usuario tiene permisos para acceder a un objeto. Las sentencias GRANT y REVOKE se utilizan para controlar el acceso de los usuarios a MySQL. Los permisos pueden darse en varios niveles:

- Nivel global: los permisos globales se aplican a todas las bases de datos de un servidor dado. Se guardan en la tabla mysql.user.
- Nivel de base de datos: los permisos de base de datos se aplican a todos los objetos en una base de datos especificada. Se guardan en las tablas mysql.db y mysql.host.
- Nivel de mesa: los permisos de mesa se aplican a todas las columnas en una tabla dada. Se guardan en la tabla mysql.tables\_priv.
- Nivel de columna: los permisos de columna se aplican a columnas en una tabla dada. Se guardan en la tabla mysql.columns\_priv.
- Nivel de rutina: los permisos de rutina se aplican a rutinas almacenadas. Se guardan en la tabla mysql.procs\_priv.

Por ejemplo, para dar el permiso SELECT sobre toda la base de datos al usuario existente francesc, escribirás el siguiente comando:

GRANT SELECT ON base\_dades.\ TO francesc@'localhost';*

Para dar más de un permiso a la vez, se deben separar las opciones con una coma. Así que para otorgar los permisos SELECT, INSERT y DELETE al usuario francesc , escribirás el siguiente comando :

GRANT SELECT, INSERT, DELETE ON base\_dades.\ TO francesc@'localhost';

Una vez que haya terminado debe refrescar los permisos de la memoria ejecutando el comando flush privileges .

Aquí puede encontrar toda la sintaxis del funcionamiento de la sentencia GRANT :

<http://dev.mysql.com/doc/refman/5.1/en/grant.html>

A continuación se muestra un ejemplo completo de gestión de permisos de acceso:

Primero entrar en la consola MySQL como root escribiendo el siguiente comando ya continuación introduzca la contraseña :

# mysql -p -u root

Enter password:

Una vez en la consola de comandos de MySQL , creará la base de datos base\_de\_dades escribiendo la siguiente sentencia :

mysql> CREATE DATABASE base\_de\_dades CHARACTER SET utf8 COLLATE utf8\_bin;

Query OK, 1 row affected (0.01 sec)

Si ahora pedimos al MySQL que nos muestre las bases de datos, base\_de\_dades aparecerá en la lista.

mysql> SHOW DATABASES;

| DATABASE |
| -- |
| information\_schema |
| base\_de\_dades |
| mysql |
| phpmyadmin |

4 rows IN SET (0.00 sec)

Ahora crearéis un usuario llamado usuari1 con la contraseña 123456.

mysql> CREATE USER 'usuari1'@'%' IDENTIFIED BY '123456';

Query OK, 0 rows affected (0.00 sec)

Primero dan el permiso de SELECT a la base de datos base\_de\_dades para el usuario usuari1.

GRANT SELECT ON base\_de\_dades.\ TO 'usuari1'@'%';

Query OK, 0 rows affected (0.00 sec)

Para comprobar los permisos de un usuario se utiliza el comando show grants for usuari1.

mysql> SHOW grants FOR usuari1


| Grants FOR usuari1@% |
| -- |
| GRANT USAGE ON \.\ TO 'usuari1'@'%' IDENTIFIED BY PASSWORD '\6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9' |
| GRANT SELECT ON `base\_de\_dades`.\ TO 'usuari1'@'%'                                                     |

2 rows IN SET (0.00 sec)

Se comprueba como aparece el permiso de SELECT, ahora añadimos los permisos de DELETE y INSERT al usuario usuari1.

mysql> GRANT DELETE,INSERT ON base_de_dades TO 'usuari1'@'%';

Query OK, 0 rows affected (0.00 sec)

Se comprueba los privilegios con el comando **show grants** y se ve como el usuario *usuari1* tiene los privilegios SELECT, INSERT, DELETE en la base de datos *base\_de\_dades*.

mysql> SHOW grants FOR usuari1;

| Grants FOR usuari1@% |
| -- |
| GRANT USAGE ON \*.\* TO 'usuari1'@'%' IDENTIFIED BY PASSWORD '\*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9' |

| GRANT SELECT, INSERT, DELETE ON `base\_de\_dades`.\* TO 'usuari1'@'%'                                     |

2 rows IN SET (0.00 sec)

Para acabar y refrescar los permisos de la memoria es necesario ejecutar el comando ***flush privileges:***

mysql> FLUSH privileges;

Query OK, 0 rows affected (0.00 sec)


# Verificación y pruebas

Para verificar el funcionamiento de MySQL puede utilizar software de monitorización que controla la disponibilidad de servicios. Para monitorizar el servicio de base de datos MySQL debe instalar conectores en el software. Entre las herramientas de software de monitorización libres que existen hablaremos de :

- `    `Nagios
- `    `Pandora FMS

## Nagios

Nagios (www.nagios.com) es un software muy popular de monitorización de redes, ordenadores y aplicaciones. Está licenciado bajo la GNU (General Public License Version 2 publicada por la Free Software Foundation) y es de código abierto.

Se puede configurar para que monitorice los equipos (hardware) y servicios (software) que el usuario quiera, alertando cuando el comportamiento de un recurso no sea correcto o supere los márgenes definidos por el administrador de red. Las alertas se pueden enviar entre otros por correo electrónico y mensajes SMS.

Entre sus características principales figuran la monitorización de servicios de red (SMTP, POP3, HTTP, NNTP, ICMP, SNMP, FTP, SSH); de sistemas de hardware (carga del procesador, uso de disco, memoria, estado de los puertos, archivos de log, temperatura ...); remota mediante túneles SSL cifrados o SSH.

También ofrece la posibilidad de programar complementos específicos para cualquier parámetro de interés de un sistema.

Puede encontrar diferentes plugins para monitorizar bases de datos MySQL y servidores. Puede encontrar un listado aquí:

http://exchange.nagios.org/directory/Plugins/Databases/MySQL

Aquí tiene un listado de algunos de los más populares:

- Elemento de lista de *picscheck\_mysql* (<http://oss.isg.inf.ethz.ch/nagiosplug>): comprueba y muestra el estado de las conexiones a un servidor MySQL.
- *check\_mysqld* (http://william.leibzon.org/nagios): permite establecer umbrales para las variables del pedido ***SHOW STATUS*** de MySQL.
- c*heck\_mysql\_health* (http://labs.consol.de / nagios / check\_mysql\_health): permite controlar muchos parámetros de una base de datos, tales como el tiempo de conexión, número de conexiones, índices, la tasa de éxito de la caché , las consultas lentas, etc.

## Pandora FMS

Pandora FMS (en inglés pandora Flexible Monitoring System, Sistema de Monitorización Flexible Pandora, *http://pandorafms.com*) es un software de código abierto publicado bajo licencia GPL2 GNU (General Public License), que sirve para monitorizar y medir todo tipo de elementos. Monitoriza de forma visual a lo largo del tiempo el estado de sistemas, aplicaciones o dispositivos.

Pandora FMS puede recoger información de cualquier sistema operativo, con software específico para cada plataforma: GNU / Linux, AIX, Solaris, HP-UX, BSD / IPSO y Windows 2000, XP y 2003.

Pandora FMS también puede monitorizar cualquier tipo de servicio de red tales como: TCP / IP, balanceadores de carga, routers, switches, sistemas operativos, aplicaciones o impresoras.

Para verificar el funcionamiento de MySQL existen módulos del propio software y conectores desarrollados. Entre los módulos encontramos:

- MySQL Monitoring: realiza un seguimiento general de MySQL.
- Mysql Cluster manager proccess: permite hacer un seguimiento de los procesos de MySQL.
- Mysql Active Connections: permite verificar las conexiones activas de MySQL.

## Pruebas de rendimiento

Algo muy importante en cualquier desarrollo web son las pruebas de rendimiento. Con ellas podrá evaluar atributos cuantitativos y cualitativos de su sistema como la fiabilidad o la escalabilidad, ya sean a nivel de software o hardware. Dentro de las pruebas, las bases de datos deben ser algo fundamental.

***Mysqlslap*** es una herramienta de diagnóstico de MySQL disponible desde la versión 5.1.4 que le permitirá realizar estas pruebas. *Mysqlslap* emula la carga de un gran número de clientes accediendo a un servidor MySQL y ofrece informes una vez terminada la prueba.

*Mysqlslap* puede generar sentencias SQL automáticamente si no se pueden utilizar las sentencias que ejecuta el sistema.

Para invocar mysqlslap puede hacerlo de esta manera:

shell> mysqlslap [opciones]

Puede encontrar aquí un listado de las diferentes opciones de *mysqlslap:*

*http://dev.mysql.com/doc/refman/5.1/en/mysqlslap.html*

*Mysqlslap* se ejecuta en tres etapas: preparación, ejecución y limpieza. En la preparación se crean las tablas y las consultas para la prueba. En la ejecución se usan más de una conexión de clientes para ejecutar la prueba. En la limpieza se eliminan las tablas si se especifica y se desconectan los clientes.

Un ejemplo lo tenemos en:

Especifique la consulta SQL (SELECT \* FROM tabla) y cree la tabla (CREATE TABLE tabla (clave int); INSERT INTO tabla VALUES (365)), especifique 50 clientes y 200 consultas seleccionadas para cada uno:

shell> mysqlslap -uroot -p --delimiter=";" \

`  `--create="CREATE TABLE taula (clau int);INSERT INTO taula VALUES (365)" \

`  `--query="SELECT \* FROM taula" --concurrency=50 --iterations=200

Una vez entrada la contraseña del usuario root mostrará unas estadísticas con los tiempos ( medio, mínimo y máximo ) de ejecución de todas las consultas:

Benchmark

Average number of seconds TO run ALL queries: 0.021 seconds
Minimum number of seconds TO run ALL queries: 0.009 seconds
Maximum number of seconds TO run ALL queries: 0.900 seconds
Number of clients running queries: 50
Average number of queries per client: 1

Especifique que *mysqlslap* cree la instrucción de consulta SQL a una tabla de dos columnas INT y tres columnas VARCHAR. Utilice cinco clientes de consulta 20 veces cada uno. No cree la mesa con la consulta para insertar los datos ( es decir, se usará el esquema de la prueba anterior y los datos ) :

shell> mysqlslap -uroot -p --concurrency=5 --iterations=20 \

--number-int-cols=2 --number-char-cols=3 \

--auto-generate-sql

Una vez entrada la contraseña del usuario *root*:

Enter password:

Benchmark

Average number of seconds TO run ALL queries: 0.016 seconds

Minimum number of seconds TO run ALL queries: 0.009 seconds

Maximum number of seconds TO run ALL queries: 0.106 seconds

Number of clients running queries: 5

Average number of queries per client: 0

Creará dos archivos uno de creación ( *creacio.sql* ) con las sentencias ( CREATE TABLE y INSERT INTO ) y otro de consultas ( *consultes.sql* ) con sentencias ( SELECT ) . Primero ejecutará el archivo de creación y luego se ejecutará el archivo con las consultas. Específicos cinco clientes, cinco veces cada uno:

mysqlslap -uroot -p --concurrency=5 \

`  `--iterations=5 --query=query.sql --create=create.sql \

`  `--delimiter=";"

Resultado:

Enter password:

Benchmark

Average number of seconds TO run ALL queries: 0.037 seconds

Minimum number of seconds TO run ALL queries: 0.037 seconds

Maximum number of seconds TO run ALL queries: 0.037 seconds

Number of clients running queries: 5

Average number of queries per client: 0
