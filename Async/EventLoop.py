import socket
from select import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

to_monitor = []


def accept_connection(server_socket: socket.socket):
     client_socket, addr = server_socket.accept()
     to_monitor.append(client_socket)
     print('Connection from', addr)
     print(to_monitor)


def send_message(client_socket: socket.socket):
    request = client_socket.recv(4096)
    if request:
        print(request)
        response = 'Hello World!\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)

to_monitor.append(server_socket)
event_loop()