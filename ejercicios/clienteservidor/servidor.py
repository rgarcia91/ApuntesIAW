import socket

# Crear un socket TCP/IP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto
servidor.bind(('localhost', 65432))

# Escuchar conexiones entrantes
servidor.listen()

print("Esperando conexión...")

# Aceptar una conexión
conexion, direccion = servidor.accept()

with conexion:
    print(f"Conectado a {direccion}")
    datos = conexion.recv(1024)
    print(f"Recibido: {datos.decode()}")
    conexion.sendall(datos)
