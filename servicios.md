# Servicios

## Consideraciones previas

Para que las aplicaciones puedan trabajar con servicios dependientes es
necesario tener estos servicios operativos por tanto antes de poder
desarrollar cualquier aplicación que dependa de algún servicio deberemos
tenerlo operativo.
En nuestro escenario de pruebas orientaremos las posibles soluciones a 
las que nos deberemos ajustar en función de nuestros contexto y 
conocimientos. Dado el amplio abanico de posibilidades esto corresponde
a otros módulos, por tanto esto sólo sirve como guia orientativa.

Los servicios que necesitaremos para probar nuestras aplicaciones serán :
- Bases de Datos
- Servidores Web
- Servidores Web con php instalado
- ...

en princio una base de datos a la cual nos conectaremos por JDBC es el
interfaz común que Java proporciona para poder conectarnos a
cualquier SGBD Relacional con dicho lenguaje de programación.

## Opciones para poner en marcha estos servicios

### Entorno Local

La instalación se hace sobre el mismo sistema operativo

1. Windows
    1. Instalación del Gestor de base de datos en local ([Mysql](https://dev.mysql.com/downloads/installer/),[Postgres](https://www.postgresql.org/download/windows/),..)
    En caso de conectar con java lo heremos po JDBC es elinterfaz común que Java proporciona para poder conectarnos a cualquier SGBD Relacional con dicho lenguaje de programación.
    2. Instalación de Servidor Web (IIS) o Apache o Apache + Php
    3. Instalación de bundle con varios componentes tipo [XAMPP](https://www.apachefriends.org/es/download.html)
2. Linux
    1. Instalación del Gestor de base de datos en local
        1. Seguir las instrucciones de la distribución Ejemplo (Ubuntu 20.04) desde repositorio canonical [Ejemplo](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-es)
        2. Instalación manual 
    2. Instalación de Apache (Apache+php)
       1. Desde la propia distribución 
       2. Instalación manual

### Entorno local virtual

En caso de querer tener aislado los servicios necesarios para vuestras aplicaciones para no "desordenar" vuestro ordenador con software que os sirve puntualmente para unas prácticas es buena idea virtualizar estos servicios

 1. Con hipervisores (VirtualBox,Hyper-V,Vmware)
    Una vez instalado el hipervisor (Recomendamos VirtualBox por compatibilidad) es seguir los pasos de un entorno local
    En este caso hay que controlar bien al arrancar la maquina virtual y el tipo de red seleccionado como se visualizan los puertos abiertos
    de la maquina virtualizada en la máquina anfitrión.
 2. Con contenedores (docker, LLX, ..)
    Una opción mas ligera y que nos permitirá mucha flexibilidad  en un futuro es la utilización de contenedores.
     Instalación de [Docker en Linux](https://docs.docker.com/engine/install/ubuntu/)
     Recordar hacer la [Postinstalación](https://docs.docker.com/engine/install/linux-postinstall/) para poder correr docker con vuestro usuario sin sudo ,mejor integración con vsc.
     Instalación de [Docker en linux repositorio Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
     Instalación de [Docker Desktop en Windows](https://docs.docker.com/desktop/windows/install/)

     Videos de repaso
      [Instalación con Docker Video](https://www.youtube.com/watch?v=AwZrEQaaYcA)
      [Introduccion a docker video](https://www.youtube.com/watch?v=CV_Uf3Dq-EU) 

 
### Entorno remoto (Servidores remotos)(Cloud)

Hoy en día muchas de las aplicaciones se despliegan en el cloud de Amazon , Azure, Google o bien en hosting remotos. Por tanto los servicios necesarios para nuestras aplicaciones pueden estar configurados allí.
En todo caso si bien tienes cuenta en alguno de estos servicios hay que seguir las guias para conectarse a sus bases de datos prestando especial atención a que si accedemos desde nuestra máquina local con una cadena de conexión y credenciales debemos comprobar que el servicio sea accesible de forma pública realizando las pruebas previas oportunas.

## Recomendación final

Cualquiera de las opciónes que escogas puede afectar a los ejemplos que se siguen en la guía sobre todo por el versionado de las diferentes bases de datos, los drivers específicos de java de estas bases de datos ,cadenas de conexión por tanto dado el posible abanico nos centraremos en dar soporte del versionado utilizado en los ejemplos.
Por todo ello os recomiendo la siguiente opción.
- Para usuarios de Windows
   Instalar VirtualBox en caso de no tenerlo y una Máquina virtual en Ubuntu 20.04 LTS donde instalaremos Docker y un contenedor llamado portainer que nos ayudará a facilitarnos las cosas. Aunque no sea necesario en primera instancia para acceder a un Mysql es aconsejable para el resto de servicios que en un futuro podamos utilizar y desplegar
 - Para usuarios de Linux
   Instalar docker y un contenedor llamado [portainer](https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux).
 - Como ejemplo instalaremos un contendedor apache php y mysql aplicando el comando en el terminal del sistema dependiendo de la práctica tendrás que hacerlo con los servicios necesarios que se te indique.
 - Otra recomendación es utilizar tags con versionado para mantener que nuestras imagenes siempre se comporten igual.

### Apache php

Podemos utilizar la versión de php con la variante para apache. Aunque tengamos [imágenes oficiales](https://hub.docker.com/_/php) de php en el hub lo ideal es utiliar una que ya tenga instalado el apache por tanto nos vamos a la sección de la documentación de sus instruccones 

php:<version>-apache

Esta imagen contiene el apache de debian conjuntamente con php (módulo mod_php) y usa mpm_prefork por defecto
   
Apache con un Dockerfile
```
FROM php:7.2-apache
COPY src/ /var/www/html/
```
Donde src/ es el directorio que contiene todo el código en PHP. Entonces, ejecuta los comandos para construir la imagen de docker:
    
```
$ docker build -t my-php-app .
$ docker run -d --name my-running-app my-php-app
```
    
Opcional
Es insteresante añadir la configuración el php.ini, aunque no es necesario.
Esta imagen  se distribuye con los ficheros de configuración por defecto php.ini-development y php.ini-production configuration .
Se recomienda usar la con the production para entornos de producción!
La configuración por defecto se puede personalizar copiando el archivo de configuración a el directorio $PHP_INI_DIR/conf.d/ .

Example

FROM php:7.4-fpm-alpine

#### Usar la configuración de producción por defecto
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

En muchos entornos de producción ,es recomendable contruir y habilitar la extensión del core OPcache para un mejor rendimiento.


#### Ejecución directa del servicio php-apacche

Sin embargo lo más rapido es utilizar el apache sin un dockerfile invocando su ejecución con ciertos parametros

Esto lo ejecutaremos en el terminal en el directorio donde se encuenta el código php que queremos ejecutar

```
$ docker run -d -p 80:80 --name my-apache-php-app -v "$PWD":/var/www/html php:7.2-apache
```

Con este comando nos ejecutará un contenedor basado en php 7.2 y apache estableciendo un enlace entre la carpeta en la que estamos  en ese momento y la carpeta donde apache  ejecuta su código , a la vez que establece un vinculo del puerto 80 de nuestra máquina con el puerto 80 del docket

Para las prácticas lo ideal es hacerlo desde los siguientes directorios dependiendo de tu elección.

Si tu código esta en /home/username/public_html
Si tu código esta en /var/www/html
La ubicación dentro de htdocs en caso de xamp

#### Instalación del módulo de php para conectarse con mysql

Dentro del contenedor tenemos unos scripts para poder habilitar las expetensiones de php que necesitemos
pudiendo ejecutarlas directamente dentro del contenedor o bien crea un dockerfile especifico para una nueva imagen.[Instalando Extensiones](https://github.com/mlocati/docker-php-extension-installer)

La forma más rapida para habilitarlo sería :

- Dentro del terminal del contenedor

```
$ docker exec -it <phpcontainerid> bash  
```
instalar la extenxión concreta

```
# docker-php-ext-install mysqli
```

habilitar el módulo php instalado

```
# docker-php-ext-enable mysqli
```

### Mysql

De igual manera que con apache podemos utilizar las imágenes oficiales de mysql o alguna de sus variantes [Repositorio Oficial](https://hub.docker.com/_/mysql)

#### Ejecución directa del servicio mysql

La sintaxis general para correr un contenedor es :
    
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
    
... donde some-mysql es el nombre que queremos asiganar al contenedor, my-secret-pw es el password para el usuario root MySQL y tag es la etiqueta que especifica la versión que queremos.
    
Por tanto dada la recomendación establecemos una versión que tendremos que tener en cuenta posteriomente para elegir la versión del driver que se conectará a la base de datos
 
``` 
    docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.31-debian
```

 Luego ya podremos para y arrancar los servicios desde el portainer o desde terminal con los comandos docker
 
 - Captura de portainer
   ![portainer.png](img/portainer.png)
 - Captura contenedores Mysql y Postgres
   ![contenedormysql_postgres.png](img/contenedormysql_postgres.png)
   
#### Comprobación desde ordenador cliente

   Una vez instalado el servicio en cualquiera de sus contextos en caso de que la aplicación que los va a utilzar nos de algún problema lo ideal es instalar un cliente de este servicio en la máquina que corra la aplicación para descartar que los errores nos vengan del servicio
   En nuestro caso al tratarse de bases de datos podemos instalar los clientes para poder crear por ejemplo la basededatos a la que se conectará nuestra aplicación:
   
   - Clientes para linux
        1. mysql ( Suele venir en los repositorios de las propias distribuciones)
   - Cliente Mysql Windows
        1. [heidisql](https://www.heidisql.com/)
        2. [Mysql WorkBench](https://www.mysql.com/products/workbench/)
        3. [dbeaver](https://dbeaver.io/)
   
