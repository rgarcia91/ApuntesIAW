import socket

# Crear un socket TCP/IP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
cliente.connect(('localhost', 65432))

try:
    # Enviar datos
    mensaje = "Hola, servidor"
    print(f"Enviando: {mensaje}")
    cliente.sendall(mensaje.encode())

    # Esperar la respuesta
    datos = cliente.recv(1024)
    print(f"Recibido: {datos.decode()}")

finally:
    print("Cerrando conexión")
    cliente.close()
