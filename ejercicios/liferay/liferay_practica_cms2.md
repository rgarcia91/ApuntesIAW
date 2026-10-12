Vamos a crear una web empresarial donde intervienen varios usuarios y con diferentes perfiles y cometidos dentro de la empresa. Para ello iniciaremos un docker liferay para su cometido.

Realizar los siguientes pasos:

- Introducir los usuarios siguientes de la empresa Clarity

| **Nombre de registro de usuario** |**Correo electrónico** |**Nombre** |**Apellido** |**Cargo** |
|:- |:- |:- |:- |:- |
|christiancarter|christian.carter@clarityVisionsolutions.com|Christian|Carter| Marketing Coordinator |
|claramurphy|clara.murphy@clarityVisionsolutions.com|Clara|Murphy| Marketing Manager |
|harperroberts|harper.roberts@clarityvisionsolutions.com|Harper|Rober|Recursos Humanos
|ianmiller|ian.miller@clarityvisionsolutions.com|Ian|Miller|it gerente |
|walterdouglas|walter.douglas@clarityvisionsolutions.com|Walter|Douglas|web desarrollador |


- Crear los grupos de usuarios de TI y recursos humanos

- Crea los siguientes roles asignandoles los permisos adecuados para su cometido.

| **Tipo** |**Título** |**Descripción** |
|:- |:- |:- |
| Regular | Administrador de contenido | Para aquellos que administran contenido en Liferay.
| Regular | Gerente de TI | Para un gerente dentro del departamento de TI.
| Regular | Desarrollador web | Rol para un desarrollador front-end dentro del Departamento de TI.
| Regular | Coordinador de marketing | Contribuyente individual del equipo de marketing.
| Sitio | Contribuidor de contenido del sitio | Rol basado en el sitio para aquellos que contribuyen al sitio.|

Recordar que para el rol de Gerente TI debe poder crear Sitios Web por tanto los permisos mínimos que tendra este rol serán:

| Permisos	| Sitios y repositorios |
|--|--|	 
| Portal| Añadir una comunidad |
| Portal | Ver menú de panel de control|
| Sitios Web | Acceder desde el panel de control|
| Sitios Web | Ver|

  Sitio Web llamado Clarity con el usuario Ian Miller que previamente le hemos asignado el rol de gerente de cuentas con sus respectivos permisos.

  - Asignar como miembros de este sitio al resto de usuarios.
  - Asignarles el rol de Contribuidor de contenido previamente creado y con los permisos oportunos para poder crear contenido
  -Configura el sitio web para poder acceder con una url como www.clarity.com
  - Modifica la pagina inicial a nuestro sitio web por defecto.

  - Crea la estructura de páginas web del sitio Clarity con la siguiente estructura:

  ![Clarity quiere implementar esta jerarquía de página para su sitio web empresarial.](../../img/liferay/Aspose.Words.5f3ba04a-e2dd-4320-bdee-832ac45207ea.066.png)

```
  |-- Home
  |-- Sign in
  |-- Contact Us
  |-- About Us -- |
                  |-- General Info
                  |-- LeaderShip Profile
  | -- Produts  -- Product List | -- Product Details
  | -- Blog     -- Blog Post
  | -- Faq      -- Faq Details
  | -- Carrears -- Open Positions --Job Opening Details
  | -- Search
  | -- Error Pages
  
   - Crea la página de contenido de Faqs como explica el temario
      - Crea un patrón
      - Crea una plantilla de página
   - Crea una plantilla de paginas de visualización de contenido
```
 Entregad un documento pdf con la captura de los resultados generados en cada paso. 