# Extendiendo Liferay

**Adaptando Gestores de Contenido**

Un gestor de contenidos es una herramienta que lejos de ser un software cerrado ofrece la capacidad de personalizarse, adaptarse y extenderse para alcanzar los objetivos que deseemos, si con lo que realiza de base el gestor de contenidos o bien con el grado de adaptación que podemos obtener a golpe de ratón no es suficiente. Para alcanzar los  resultados o la funcionalidad deseada disponemos de módulos o en el caso del gestor seleccionado plugins realizados por terceras personas, bien libres de comunidad o bien de pago, que nos permiten ampliar funcionalidades que no vienen en el producto  inicialmente.

## Plugins
Por tanto la estrategia inicial en el caso que nos haga falta alguna ampliación, es aprender a instalar esta serie de plugins que nos permitirán alcanzar nuestros objetivos.

Para ello debemos saber qué tipos de adaptaciones o funcionalidades nos hacen falta.

En liferay tenemos los siguientes tipos de módulos o plugins.

### Themes
Son los encargados de cambiar todo el aspecto del portal, es decir la parte visual e incluso interactiva ya que también recogen todo el javascript.

Con la finalidad de ser lo más sólidos y robustos posible todos parten como adaptaciones de uno base.

Las características principales son:

- Los themes sólo deberían contener las diferencias respecto al theme que extienden
- Con la 6.2 los themes son responsivos y utilizan bootstrap, por ejemplo el theme base "Classic"
- De forma general la construcción de temas seguiría los siguientes pasos
  1. Compilar el tema para la 6.2
  1. Comprobar el funcionamiento y sus logs
  1. (Opcional) Actualizar el tema para que sea responsivo
  1. (Opcional) Empezar el tema desde cero con bootstrap
  
### Layouts
Son los encargados de definir la distribución que tienen las páginas web que se crean en el portal, es decir columnas y filas que se disponen en una página.

- Ahora incorporan bootstrap y scaffolding
- Deberían funcionar sin problema con solo compilar para 6.2 sin ser responsivos
- Es recomendable por su facilidad rehacerlos desde cero

### Portlets
Son los módulos o unidades funcionales que nos permiten añadir aplicaciones en el portal obteniendo así toda la funcionalidad que cualquier sistema de programación es capaz de darnos. Sus características principales son:

- Ahora disponen de nuevas API
- Algunas clases y métodos de la API han podido ser deprecados y deberían ser reemplazados
- Se han añadido nuevas funciones que podrían ser útiles: ADT, papelera reciclaje, sandboxing, ...
  1. Compilar el portlet para la versión 6.2
  1. Comprobar el funcionamiento y sus logs
  1. (Opcional)  Añadir responsive design
  1. (Opcional) Volver a compilar y comprobar el funcionamiento
 
### Hooks
Este tipo de extensión nos permite modificar puntos de conexión más internos que afectan a ciertos puntos controlados del portal permitiéndo hacerlo más integrable con herramientas de terceros

- Nuevos tipos de hook disponibles
- Más potencia y acceso
- Se deployan en tiempo de ejecución
- Los hooks pueden afectar al proceso de actualización, es importante que no estén instalados en ese momento
- Los hooks pueden tener una fuerte dependencia con la versión del portal
  1. Se recomienda comprobar uno a uno los ficheros (jsps, clases, properties, ...) que modifica el hook con el portal actual respecto la versión anterior.
     Se pueden comparar directamente los ficheros que modifica entre las versiones oficiales del portal, puede ser más fácil que directamente con el hook
  1. En caso que los ficheros originales que modifica el hook difieran de una versión de portal a la otra se debe rehacer el funcionamiento de esa parte para la nueva versión
  1. Compilar el hook para la versión 6.2
  1. En hooks agresivos (modifican permisos, documentos, contenidos, etc) es recomendable probar su funcionamiento con una versión limpia de la versión del portal
  1. Comprobar el funcionamiento y sus logs


### Ext / Extlet
Este tipo de módulo nos permite reemplazar totalmente trozos de código del portal original permitiendo que el portal original se comporte de otra manera totalmente diferente. Su desarrollo exige un gran nivel técnico así como conocimientos grandes del funcionamiento del código de liferay.

- Se recomienda evitarlos y reemplazar los que haya por portlets y/o hooks.
- Para deployarse correctamente necesitan el reinicio del servidor
- Pueden afectar al proceso de actualización, es importante que no estén instalados en ese momento
  1. Pensar si puede ser reemplazado por un portlet y/o hook, en caso afirmativo crear uno desde zero.
  1. En caso negativo adaptarlo a los nuevos ficheros del portal, se deberá comprobar cada fichero que modifique si ha cambiado en la nueva versión respecto la anterior
  1. Compilar el ext plugin para la versión 6.2
  1. Instalar y reiniciar el servidor


## Estrategias de adaptación
Una vez introducido este tipo de módulos lo más lógico es que si con el nivel de adaptación del gestor de contenido a golpe de ratón no hemos alcanzado el aspecto o la funcionalidad deseada pasemos a buscar si existe el módulo o la adaptación necesaria realizada por algún tercero.

Para ello el punto de inicio es un Marketplace que Liferay mantiene para toda la comunidad de desarrolladores y partners o socios tecnológicos donde se encuentran infinidad de plugins tanto libres como de pago.

Podemos navegar y consultar este sitio accediendo a la página; <https://web.liferay.com/es/marketplace>

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.001.png)

Aquí podemos buscar cualquier tipo de extensión filtrando por algunos criterios. Los principales para las pruebas que queremos realizar es la versión de liferay para la que están creados o adaptados y la no menos importante que sean gratuitos.


### Temas (Themes)
Es habitual adaptar la apariencia que el portal ofrece de base para darle una personalidad o atractivo acorde al producto o servicio  al que está destinado el portal.

En principio elegiremos un tema de apariencia que nos lo descargaremos del marketplace. Nos tendremos que dar de alta con nuestra cuenta de correo en el marketplace para que permita bajarnos los plugins de apariencia (theme)

Una vez descargado en nuestro sistema de archivos en la máquina virtual debemos desplegarlo o instalarlo.

Para arrancar partimos de nuestro portal instalado en la práctica anterior y accederemos con el usuario que nos creamos con privilegios de administrador.

Una vez aquí iremos a la opción Administración / Panel de Control

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.002.png)

Aquí nos meteremos en Aplicaciones Gestor de aplicaciones

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.003.png)Procedemos a examinar la ubicación del archivo que acabamos de descargar para proceder a su instalación

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.004.png)

La forma de saber que todo ha ido bien para poder aplicar esta nueva adaptación en el aspecto es accediendo a cualquier sitio web que tengamos previamente creado y acceder a paginas del sitio web donde podremos comprobar que el aspecto que tiene este sitio corresponde con el tema actual classic

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.005.png)Si nos desplazamos en esta ventana a la parte inferior nos aparecerá la posibilidad de cambiar el aspecto de este sitio seleccionando el tema que acabamos de instalar, en el ejemplo el que pone gva.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.006.png)

Una vez seleccionados los cambios de aspecto nuestro sitio web se mostrará con los cambios en toda su esencia.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.007.png)

### Layouts  (Distribuciones en la página)
Los layouts nos ayudan a diseñar o estructurar las diferentes secciones donde se mostrarán las aplicaciones en una página. En el caso de que liferay de base no nos ofrezca una distribución que se adapte a nuestras necesidades podemos buscar en el marketplace para proceder a instalar una.

En este caso el filtro con el que buscaremos en el marketplace es estructuras de página.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.008.png)

Seleccionaremos una de ellas y la compraremos de forma gratuita como hicimos con el tema de apariencia anterior.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.009.png)

Una vez descargada instalamos siguiendo los mismos pasos.

Para comprobar que ha sido correctamente instalada deberemos ir a una página y cambiar su distribución.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.010.png)

Una vez seleccionada la nueva distribución para la página actual procederemos a cambiar las aplicaciones que se muestran en la página manteniendo apretado el ratón sobre la parte superior de la ventana que contiene la aplicación y arrastrándola sobre otra posición.

### Aplicaciones  (Portlets)
Liferay viene con muchos módulos o aplicaciones de base que podemos probar de forma sencilla añadiéndolas a sus páginas desde los botones + Añadir.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.011.png)

Seleccionando por las diferentes categorías de aplicaciones encontramos módulos que se van instalando en nuestras páginas ofreciéndonos nuevas funcionalidades.

Si después de probar éstas no obtenemos ninguna que satisfaga la necesidad que estamos buscando podemos ir al marketplace e instalarnos una de forma similar a lo que hemos realizado con el tema de apariencia.

Esta vez en el filtro de la búsqueda pondremos la versión 6.2 CE GA6 , Gratis y Apps

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.012.png)


Seleccionaremos uno de los portlets para probar su instalación en el ejemplo utilizaremos uno para integrar videos de youtube.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.013.png)Una vez descargado el archivo pasamos a realizar la instalación de la misma manera que lo hicimos con el módulo de relación de aspecto.

Una vez incorporado siguiendo los pasos de instalación añadiremos este portlet o aplicación a nuestra página de bienvenida.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.014.png)

Procederemos ahora a configurar la aplicación con los datos requeridos para que nos muestre un video de youtube haciendo clic en la rueda que aparece en la parte superior derecha donde hemos puesto la aplicación en nuestra página

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.015.png)

En este punto sólo nos queda configurar los datos necesarios de la url del video a visualizar en youtube y algunas preferencias.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.016.png)

Quedando finalmente integrada en nuestra página web con el siguiente aspecto

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.017.png)

Podemos probar instalando varias aplicaciones mas.

### Hooks
En muchas ocasiones no sólo queremos añadir un nuevo aspecto, una distribución de página nueva sino que realmente queremos que liferay se integre con algún sistema externo o bien modifique algún aspecto relacionado con la forma de trabajar subyacente en el portal. Para ello nos dota de hooks o ganchos que nos permite extender estos puntos de control.

Liferay dispone de aplicaciones para gestionar documentos. Los archivos de sus bibliotecas se guardan en el propio servidor donde reside su almacenamiento. Podemos tener necesidad de que liferay se integre con los documentos que existen en google drive. Esto es una modificación que cambia y extiende el comportamiento normal de este gestor de contenido. Para conseguir esto de  nuevo buscamos en el marketplace de liferay esta vez buscando por palabras la palabra google

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.018.png)

Como vemos aparecen diferentes app que nos permiten integrarnos con aplicaciones de google.

Vamos a proceder a integrar un repositorio de Google Drive en nuestro portal.(Los pantallazos pueden variar según las actualizaciones de google por lo que no lo incluiremos como práctica aunque es interesante conocer su potencial)

Esta aplicación cambia el comportamiento normal del portal y modifica secciones de configuración en varios sitios como la clave del api necesaria de google para que liferay pueda conectarse y la aplicación de documentos para poder añadir y visualizar los documentos que se depositan en Google Drive.

Nos descargamos la aplicación de la misma forma que lo hemos realizado en ocasiones anteriores y la instalamos. Este tipo de hooks  dada su complejidad suele ir acompañado de algunos requerimientos de configuración.

Este en concreto nos requerirá que habilitemos el acceso al api de google drive así como crear un id de cliente y una clave secreta en google.

Para ello seguimos los siguiente pasos para manejarnos con  Google Drive API and Oauth:

0. Ir a <https://console.developers.google.com/project>.

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.019.png)
1. Click en ‘Proyecto botón 'Crear Proyecto' acabarás en el asistente Google Developers Console

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.020.png)
2. Click en el enlace 'Credenciales' en el menu de la izquierda
3. Cick en 'Crear credenciales tipo Client ID Oauth '

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.021.png)

4. Saltará la pregunta de tipo de aplicación

5. Selecciona 'Aplicación Web' y consiente los términos

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.022.png)6. Pon el correo de gmail utilizado en la quincena anterior y rellena un nombre  'liferay'

7. Guarda – Se presentará una pantalla similar donde deberás rellenar 'Authorized Javascript origins' y'Authorized redirects URIs'

8. Rellena el nombre del portal. (Como accedemos con localhost en nuestro caso pondremos (e.g. http://localhost:8080) en el campo’Authorized Javascript origins'

9. Rellena el nombre del portal precedido de la cadena '/c/document\_library/google\_api\_access?cmd=token' en el campo 'Authorized redirects URIs' (e.g. [http://](http://localhost:8080/c/document_library/google_api_access?cmd=token)[localhost:8080](http://localhost:8080/c/document_library/google_api_access?cmd=token)[/c/document_library/google_api_access?cmd=token](http://localhost:8080/c/document_library/google_api_access?cmd=token))

10. Apretar 'Crear Client ID'  - veras 'Client ID web application' Necesitaras recordar:

a) Client ID

b) Client secret

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.023.png)

11. Haz click en  'Biblioteca' en el menú de la parte izquierda – se presentaran las  'API library'

12. Haz click en  'Drive API'

13. Habilitalá con el botón.

14. Ahora tenemos que ir al portal

15. Ir a  'Panel de control' -> 'Configuración del portal' -> 'Autenticación'

![](img/Aspose.Words.f1fbc94a-b082-42d9-9692-853ca4ed550f.024.png)

16. Click en sección 'Google'

17. Rellenamos  el 'Client ID' y 'Client secret' del paso anterior.

18. Click en  'get Access & Refresh Token' que nos redirigirá a Google

19. En el emergente seleccionamos el correo de la cuenta con drive () donde queremos almacenar los documentos compartidos

20. Consentimos  'Aceptando'

a) cuenta de correo

b) perfil básico de datos

c) Gestión de los datos de drive

21. Vamos a Administración /Contenidos/Documentos y Multimedia
22. Le damos al botñon de Añadir y seleccionamos repositorio'
23. Rellenamos el nombre 'Google Repository' como 'Tipo'

24. Guardamos

25. Creamos las carpetas y documentos sobre ella

26. Para comprobar que se crean en drive entraremos por la web e identificaremos que nos ha creado una carpeta con un identificador numérico donde dentro estarán las carpetas.


### **Ext / Extlet**
Finalmente si necesitamos una ampliación o modificación de la cual tenemos que tocar necesariamente las fuentes del portal disponemos de este tipo de extensiones, éstas requieren un nivel de conocimientos profundo deben realizarse por personal muy experto en la plataforma.
