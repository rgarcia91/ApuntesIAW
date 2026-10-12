# Visual Studio Code para PHP

Visual Studio Code es uno de los mejores editores de código fuente (si no el mejor). Es simple, rápido y además tiene muchas características como autocompletado (Intellisense), asistente de sintaxis, snippets y la posibilidad de añadir extensiones.

- Necesitamos descargar Visual Studio Code desde su página web [Download](https://code.visualstudio.com/download)
- Una vez instalado podremos ver un asistente que nos permitirá ajustar el editor con algunas extensiones y opciones que nos ayudarán en nuestros propósitos

![Imagen1](/img/vsc1.png)

- En nuestro caso como queremos utilizarlo con php le añdiremos una extensión llamada  PHP Intelephense

![Imagen2](/img/vsc1.png)

## Configurar Visual Studio Code para PHP ##

Visual Studio Code utiliza el propio motor de PHP para interpretar la sintaxis del lenguaje de programación. Esto puede sonar trivial, pero es una buenísima noticia ya que esto permite que VS Code para PHP esté siempre a la última.

Para permitir que nuestro Visual Studio Code nos proporcione toda la potencia de PHP, lo primero que tenemos que hacer es modificar los Ajustes para decirle a VS Code dónde está instalado PHP.

Para ello, una vez abierto Visual Studio Code, vamos a Archivo -> Preferencias -> Ajustes (File -> Preferences -> Settings), o utilizamos el atajo de teclado «Control+,». Esto nos abrirá el panel de Ajustes que debemos modificar a continuación.

![Imagen3](/img/vsc3.png)

Escribimos «php» en la barra superior para filtrar los ajutes y sólo mostrar los que necesitamos:

![Imagen4](/img/vsc4.png)

En este panel de ajustes, debemos asegurarnos que las opciones de Php Validate «Enable» y «Run» estén marcadas. Tras esto, vamos a modificar el fichero settings.json para incluir la ruta al ejecutable de PHP que tenemos instalado en nuestro ordenador.

Nota: Si no tienes PHP instalado, necesitarás instalarlo previamente.

![Imagen5](/img/vsc5.png)

La ruta dependerá del Sistema Operativo que estés usando (Windows, Linux o Mac).

Llegados a este punto, ya podemos utilizar nuestro Visual Studio Code como IDE para desarrollar en PHP.

## Extensiones PHP en Visual Studio Code

Antes de crearnos nuestro primer Hello World con PHP en Visual Studio, os recomendamos instalar las siguientes extensiones para el IDE que os harán la vida mucho más fácil.

- PHP IntelliSense: proporciona autocompletado de código según vayamos escribiendo.
- PHP Debug: nos permite añadir puntos de interrupción e inspeccionar nuestro código y variables en tiempo real mientras se ejecuta.
- PHP Extension Pack: contiene las dos anteriores 
    
 ![Imagen6](/img/vsc6.png)
 
 Para ello debemos pinchar en el botón de extensiones del menú lateral izquierdo, y filtrar por «php». Pinchamos en el botón «Install» para cada una de ellas, y listo.
 
## Debug PHP en Visual Studio Code ##

Depurar nuestro código PHP con Visual Studio Code es más fácil que nunca gracias a la extensión PHP Debug que hemos comentado en la sección anterior.

Es muy importante el hecho de poder hacer debug de nuestro código, ya que podremos parar la ejecución con puntos de interrupción (breakpoints) que nos permitirán ver el valor de variables y/o entender la forma en que ejecuta nuestro código.

Para comprender bien cómo funciona la depuración en VS Code os recomendamos echar un vistazo a esta [guía](https://code.visualstudio.com/docs/editor/debugging) publicada en la web de Visual Studio.
    
## HelloWorld en PHP con Visual Studio Code

Llegados a este punto, ya tenemos listo nuestro Visual Studio Code para comenar a desarrollar PHP

Lo primero que tenemos que hacer, como siempre que utilizamos VS Code, es abrir una Carpeta o Espacio de trabajo (Workspace) para comenzar a trabajar.

![Imagen7](/img/vsc7.png)

En mi caso, creo una nueva carpeta HelloWorldPHP (de momento vacía) y la selecciono. A continuación, creamos un nuevo fichero llamado index.php y que será el punto de entrada de nuestra web en PHP.

![Imagen8](/img/vsc8.png)

Para verlo en el navegador, podemos hacer botón derecho sobre el fichero index.php y abrirlo con cualquier navegador (Chrome, Firefox, Safari, etc). De momento esto nos servirá, ya que aún no hemos añadido código PHP

![Imagen9](/img/vsc9.png)

Finalmente, vamos a probar a introducir código PHP en nuestra web, para comprobar que toda la configuración de Visual Studio Code es correcta. Por ejemplo, podemos probar a mostrar en nuestra página web información sobre la instalación de PHP (versión, etc).

![Imagen10](/img/vsc10.png)

Como veis, el código PHP se introduce entre las etiquetas <?php y ?>, ya que es la sintaxis típica de PHP. Mientras escribimos dentro de estas etiquetas, tenemos ayuda por parte de la extensión de IntelliSense que hemos activado previamente, de forma que no tenemos que aprendernos de memoria todas las funciones disponibles en PHP.

## Utilizar un servidor local de PHP

Tras introducir código PHP en el fichero index, te habrás dado cuenta de que no se visualiza en nuestro navegador. Esto es porque el código PHP necesita un servidor para poder ser ejecutado, así que ya no vale símplemente con abrir el fichero index.php con nuestro navegador.

Esto no será necesario cuando estemos desplegando nuestra web PHP en un servidor, pero sí en nuestro ordenador o PC local de desarrollo.

Un workaround rápido es abrir con un Explorador de Archivos la carpeta donde está nuestro index.php, y levantar una Terminal/Consola/Powershell. A continuación escribimos el comando:

![Imagen11](/img/vsc11.png)

Y en ese momento ya tendremos un servidor local que es capaz de ejecutar nuestra web PHP en la dirección http://localhost:8001 (en vez de 8001, puedes elegir el puerto que quieras que no esté ocupado).

![Imagen12](/img/vsc12.png)

## Control de versiones

Dentro de las funcionalidades mas destacadas de este editor destaca la integración con el control de versiones. Una vez instalado git en nuestro sistema podremos verlo integrado en el propio editor

## Gestión de repositorios remotos Github

Continuando con las funcionalidad arriba expuesta tambien nos permite automatizar las copias en nuestros repositorios remotos

Una vez en el directorio donde tenemos el proyecto podemos inicializar la subida al repositorio remoto

![Imagen12](/img/vsc_git_github.png)

Nuestros directorivos de trabajo dependerán de donde tenemos nuestro código y esto por praticidad los generaremos en las rutas donde se pone el código en nuestros servidores web locales de pruebas
- Apache sobre Ubuntu (Aunque normalmente esta en la ruta /var/www/html esta carpeta tendriamos que ir cambiando permisos por eso activaremos el modulo userdir siguiendo los pasos en los apuntes por tanto la carpeta donde pondremos el código es en mi home de usuario subcarpera public_html la cual sincronizaremos con mi repositorio de github
- Windows dependerá si hemos escogido un xamp deberemos localizar la carpeta htdocs donde normalmPente se guarda el código

Crearemos un archivo index.php con un ejemplo básico de Hola mundo en la carpeta oportuna

Pasos para realizar la creación del repositorio remoto con tu cuenta de github. Una vez abierto el Visual Studio Code en la carpeta public_html le damos al icono del panel izquierdo donde nos muestra la vista de control de versiones donde nos aparecera la opción de crear el repositorio en github.
Nos pedirá que nos registremos en gitgub con nuestra cuenta solicitando los permisos oportunos. Nos mostrara el nombre de repositorio a crear que coincide con el de la carpeta.

![Creación Repositorio desde vsc](/img/vcs_github1.png)

Nos creará el repositorio que podremos comprobar accediendo a la web y visualizando el código
![Web repositorio creado](/img/vcs_github2.png)

Ya podemos realizar los cambios en nuestro código
Realizaremos una pequeña modificación para subir un commit
Al revisar el estado de la carpeta bajo la vista de versiones nos aparecerá en pendiente de stage
![Fichero staged](/img/vcs_github3.png)

Le damos para confirmar los cambios pero aún no está en el repositorio remoto sólo en el local.
Confirmamos el commit con un mensaje y ya podemos comprobar que nuestro archivo esta en el reposio remoto
![Commit al repositorio](/img/vcs_github4.png)

Nota: Para agilizar nuestro trabajo podemos suponer que cualquier modificación de archivo supone el paso al staged

## Conclusiones

En este artículo hemos visto cómo configurar Visual Studio Code para PHP. Es un tema muy interesante ya que VS Code es uno de los editores de código fuente más potentes y ligeros que existen a día de hoy.

La experiencia de desarrollo con Visual Studio Code es una de las mejores que he tenido. entre todos los IDE que he probado, así que espero que os haga la vida un poco más fácil a la hora de desarrollar vuestras webs en PHP.
