import socket

# Set up a basic server to simulate communication with edge devices
def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Binding to localhost and port 12345
    server_socket.listen(5)  # Listen for incoming connections
    print("Server listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024)  # Receive data from the client
        print(f"Data received: {data.decode()}")

        client_socket.send(b"Data received")  # Send acknowledgment
        client_socket.close()

# Start the server (run in a separate terminal)
# create_server()
