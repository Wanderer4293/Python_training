import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind(('localhost', 5555))
client_socket.connect(('localhost', 5000))

while True:
    message = input().encode()
    request = client_socket.sendall(message)
    response = client_socket.recv(4096)
    print(response)