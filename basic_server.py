import socket

#basic socket setup
OUR_IP = '127.0.0.1'
OUR_PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((OUR_IP, OUR_PORT))
server_socket.listen(5)

print(f"[*] Listening on {OUR_IP}:{OUR_PORT}")

#vars for number of acks, and number of connections
ackNum = 0
numConnection = 0

#main server loop
while True:

    #accepts one connection for testing purposes
    if numConnection == 0:
        client, addr = server_socket.accept()
        numConnection +=1

    #recieve message from client
    message = client.recv(1024).decode('utf-8')
    print(message)

    #send back an ack with an id
    ack = f"ACK{ackNum}!"
    client.send(bytes(ack, 'utf-8'))
    ackNum += 1