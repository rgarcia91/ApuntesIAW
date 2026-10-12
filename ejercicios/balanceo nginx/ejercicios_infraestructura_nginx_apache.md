
# Ejercicios para Evaluar la Tolerancia a Fallos y el Rendimiento de la Infraestructura

## Descripción de la Infraestructura
Esta infraestructura se basa en un servidor Nginx que balancea la carga entre dos servidores Apache. Utilizando `docker-compose`, se despliegan tres servicios (Nginx, Apache1 y Apache2), conectados en una red compartida.

### Ejercicio 1: Prueba de Tolerancia a Fallos
#### Objetivo
Comprobar la capacidad de la infraestructura para seguir respondiendo a las solicitudes cuando un servidor Apache falla.

#### Pasos:
1. **Levanta la infraestructura**: Ejecuta el siguiente comando para levantar todos los contenedores:
   ```sh
   docker-compose up -d
   ```
2. **Verifica la conectividad**: Abre un navegador o usa `curl` para comprobar que el servidor Nginx está respondiendo correctamente en `http://localhost:8080`.
   ```sh
   curl http://localhost:8080
   ```
3. **Detiene un servidor Apache**: Apaga uno de los servidores Apache para simular un fallo.
   ```sh
   docker-compose stop apache1
   ```
4. **Comprueba la respuesta del balanceador**: Intenta acceder nuevamente a `http://localhost:8080` y verifica si el servidor sigue respondiendo. Esto confirmará si Nginx está redirigiendo el tráfico al servidor Apache restante.
5. **Levanta de nuevo el servidor Apache**: Vuelve a levantar el contenedor detenido.
   ```sh
   docker-compose start apache1
   ```
6. **Verifica la recuperación**: Comprueba que la infraestructura se ha recuperado completamente y que Nginx balancea las solicitudes entre ambos servidores.

### Ejercicio 2: Prueba de Rendimiento con Apache Bench (`ab`)
#### Objetivo
Evaluar el rendimiento del balanceador de carga bajo diferentes niveles de solicitudes concurrentes.

#### Pasos:
1. **Instala Apache Bench**: Si aún no lo tienes, instálalo (en sistemas basados en Debian):
   ```sh
   sudo apt-get install apache2-utils
   ```
2. **Prueba de carga**: Utiliza Apache Bench para enviar un gran número de solicitudes concurrentes a Nginx:
   ```sh
   ab -n 1000 -c 50 http://localhost:8080/
   ```
   - `-n 1000`: Número total de solicitudes.
   - `-c 50`: Número de solicitudes concurrentes.
3. **Analiza los resultados**: Observa el tiempo de respuesta promedio, la cantidad de solicitudes fallidas, y la velocidad de procesamiento. Estos datos te permitirán entender cómo maneja la infraestructura un número alto de solicitudes.

### Ejercicio 3: Fallo en el Balanceador Nginx
#### Objetivo
Determinar el impacto de un fallo en Nginx y cómo restaurar el servicio.

#### Pasos:
1. **Detiene Nginx**: Para simular un fallo en el balanceador, detén el contenedor de Nginx.
   ```sh
   docker-compose stop nginx
   ```
2. **Intenta acceder al servicio**: Intenta acceder nuevamente a `http://localhost:8080`. Verifica que el servicio no está disponible, lo cual indica que Nginx es un único punto de fallo.
3. **Levanta Nginx de nuevo**: Vuelve a iniciar el contenedor de Nginx para restaurar el servicio.
   ```sh
   docker-compose start nginx
   ```
4. **Verifica la recuperación**: Asegúrate de que Nginx está balanceando nuevamente las solicitudes entre los dos servidores Apache.

### Ejercicio 4: Simulación de Sobrecarga y Monitoreo
#### Objetivo
Observar cómo la infraestructura responde a una sobrecarga y cómo se distribuyen las solicitudes entre los servidores Apache.

#### Pasos:
1. **Herramienta de monitoreo**: Utiliza `docker stats` para monitorear el uso de recursos de cada contenedor.
   ```sh
   docker stats
   ```
2. **Genera tráfico constante**: Utiliza herramientas como `ab` o `siege` para generar un alto volumen de tráfico durante un período prolongado de tiempo:
   ```sh
   ab -n 5000 -c 100 http://localhost:8080/
   ```
3. **Observa el balanceo de carga**: Mientras se genera tráfico, monitorea los contenedores Apache para verificar si ambos están recibiendo un número de solicitudes similar, lo cual indicará un balanceo de carga efectivo.
4. **Ajustes de Nginx**: Opcionalmente, modifica el archivo `nginx.conf` para experimentar con las configuraciones de `upstream`, como habilitar `least_conn` para balancear según el menor número de conexiones activas:
   ```nginx
   upstream backend {
       least_conn;
       server apache1:80;
       server apache2:80;
   }
   ```
   Luego, recarga Nginx y verifica cómo cambian los resultados.

### Ejercicio 5: Escalabilidad
#### Objetivo
Agregar un nuevo servidor Apache y evaluar cómo afecta el rendimiento.

#### Pasos:
1. **Modificar el archivo `docker-compose.yml`**: Añadir un nuevo servicio Apache (e.g., `apache3`) al archivo `docker-compose.yml`.
2. **Modificar el archivo `nginx.conf`**: Añadir la nueva instancia Apache al `upstream` en el archivo `nginx.conf`.
3. **Levantar la infraestructura actualizada**:
   ```sh
   docker-compose up -d
   ```
4. **Repetir pruebas de rendimiento**: Repite las pruebas de rendimiento utilizando `ab` o `siege` y observa si la adición de un tercer servidor Apache mejora el tiempo de respuesta y la capacidad del sistema.

Estos ejercicios te permitirán explorar cómo funciona la infraestructura en situaciones de fallo, cómo responde al estrés y qué tan bien distribuye la carga entre los servidores disponibles. Además, te ayudará a identificar posibles puntos de fallo y maneras de mejorar la tolerancia y escalabilidad del sistema.
