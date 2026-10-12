---
marp: true
theme: default
paginate: true
backgroundImage: url('img/fondo.png')
header: Implantación de aplicaciones Web. Tema 1.
footer: IES Camp de Morvedre - Curso 24/25
---

# Introducción

Internet es la principal herramienta de intercambio de información. La conexión de ordenadores a redes locales y globales permite la comunicación global.

---

# Servicios Web

Para ofrecer servicios web, los servidores deben tener:

- Servidores web para enviar contenidos.
- Preprocesadores de hipertexto (PHP) para contenidos dinámicos.
- Servidores de bases de datos para almacenar información.

---

# Análisis de Requerimientos

Un servidor web responde a las peticiones de los navegadores y entrega páginas a través de Internet.

---

## Protocolos

La comunicación entre el navegador y el servidor se realiza mediante:

- **TCP**: asegura que el mensaje llegue sin errores.
- **IP**: encuentra el camino hasta el servidor.
- **HTTP**: protocolo usado para pedir el recurso.

---

# La URL

Una URL accede a un recurso en un servidor. Ejemplo: <https://aules.edu.gva.es/fp/login/index.php>

- **Protocolo**: HTTPS
- **Dirección del servidor**: aules.edu.gva.es
- **Puerto**: 443 (HTTPS), 80 (HTTP)
- **Ruta**: fp/login/
- **Recurso**: index.php

---

# Comunicación Cliente-Servidor

El navegador se comunica con un servidor DNS para obtener la IP del dominio y se conecta al puerto 443 del servidor.

---

## Petición y Respuesta

El navegador envía una petición al servidor solicitando el recurso. El servidor procesa la petición y devuelve la página solicitada.

---

## Métodos GET y POST

- **GET**: envía información en la URL (limitada y pública).
- **POST**: envía información en el contenido (no visible directamente).

---

## Práctica. Instalación máquina virtual Debian
## Práctica. Instalación docker-desktop en Ubuntu

https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/
https://docs.docker.com/desktop/install/linux/ubuntu/
