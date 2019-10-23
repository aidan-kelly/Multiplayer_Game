import socket

OUR_IP = '127.0.0.1'
OUR_PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((OUR_IP, OUR_PORT))
server_socket.listen(5)

print(f"[*] Listening on {OUR_IP}:{OUR_PORT}")

numConnection = 0
while True:
    if numConnection == 0:
        client, addr = server_socket.accept()
        numConnection +=1

    message = client.recv(1024).decode('utf-8')
    print(message)
