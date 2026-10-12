# Mysql Instalación

La forma más sencilla de instalar MySQL  es mediante apt-get . Tenéis que instalar los paquetes mysql-cliente y mysql-server. (Estos son metapaquetes que os instalarán la versión recomendada para la distribución que no tiene porque ser la última. 
    
Normalmente las versiones de Ubuntu Lts anteriores a la 18.04 suele traer una versión 5.X bastante extendida. Las versiones de Ubuntu Lts 20.04 en adelante ya han incorporado la versión 8.X (Esto hay que tenerlo en cuenta cuando la aplicación que queramos instalar tenga alguna dependencia de versión.
Para nuestras pruebas inicialmente no será relevante.


Sin embargo, Debian en la versión 12.7 ya no incluye Mysql en sus repositorios por lo que es necesario descargar configurarlo del repositorio oficial.

Para ello vamos https://dev.mysql.com/downloads/repo/apt, y descargamos e instalamos el paquete deb. Una vez instalado será necesario refrescar.

```bash
sudo apt-get install ./mysql-at-config.XXXX_all.deb  //instalando si es posible el repo de una versión LTS
sudo apt-get update
sudo apt-get install mysql-server
```   
En función de la distribución y la versión os puede pedir que contraseña asignar al usuario root de MySQL. MySQL tiene sus propios usuarios, que son independientes de los usuarios del sistema Linux. Por lo tanto **es importante guardar la contraseña de root.** si lo ofrece en la instalación
    
Con la instalación se añaden una serie de programas que nos permiten gestionar de forma eficiente diferentes aspectos de la base de datos. [Utilidades](https://dev.mysql.com/doc/refman/8.4/en/programs-overview.html)

Destacar dos programas del lado del cliente como:
**mysqladmin** y **mysql**

Si más adelante queréis volver a **cambiar la contraseña** lo podéis hacer con la orden:

```
# sudo mysqladmin -u root -h localhost password ’clave’
```

Podéis cambiar *localhost* por el nombre de la máquina. Una vez hecho ésto, ya podéis entrar al servidor MySQL con la orden:

```#sudo mysql -u root -p```

**Para parar o poner en marcha el servidor de MySQ**L tenéis el script que lo controla en **/etc/init.d/mysql** que acepta las típicas opciones (*start*, *stop*, *restart*).

Aseguraos que tenéis instalado el paquete **php7-mysql**  puesto que lo necesitaréis para trabajar con MySQL y PHP. Lo podéis


## Conexiones root mysql

En algunos sistemas como Ubuntu, MySql usa el plugin auth_socket por defecto

Basicamente esto significa que :los db_users que lo utilizan serán autenicado por las credenciales del sistema. Puedes observar que el usuario root esta establecido así. 

Como es una nueva instalación se debe hacer con sudo.
```sudo mysql -u root```


```
mysql> USE mysql;
mysql> SELECT User, Host, plugin FROM mysql.user;

```
| User | plugin |
| ---- | ------ |
| root | auth_socket |
| mysql.sys | mysql_native_password |
| debian-sys-maint | mysql_native_password |

Como puedes ver en la query, el usuario root esta utilizando auth_socket plugin.

Hay varias opciones para resolver este problema:

    Podemos establecer que el usuario root use mysql_native_password plugin
    Puedes crear un nuevo db_user con tu usuario de sistema

Opción 1:

```
sudo mysql -u root # Se debe usar "sudo" ya que es una nueva instalación

mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;

sudo service mysql restart

```

Opción 2: (Remplazar tu usuario de sistema con tu nombre de usuario)

```
sudo mysql -u root # Se debe usar "sudo" ya que es una nueva instalación

mysql> USE mysql;
mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY 'YOUR_PASSWD';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;

sudo service mysql restart

```
Recuerda que si usas la opción #2 deberás conectar con Mysql con tu nombre de usuario 
Remember that if you use option #2 (mysql -u YOUR_SYSTEM_USER).

Nota: En algunos sistemas (e.g., Debian 9 (Stretch)) el 'auth_socket' plugin es llamado 'unix_socket', asi que el comando SQL debe ser: UPDATE user SET plugin='unix_socket' WHERE User='YOUR_SYSTEM_USER';

En MySQL 8.x.x se ha cambiado auth_socket a caching_sha2_password para los dbusers que no son el root
