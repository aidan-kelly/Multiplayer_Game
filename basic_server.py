#!/usr/bin/env python3

import socket
import threading

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
clients = []

def handleClient(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
        for c in clients:
            if c.getpeername() != client_socket.getpeername():
                #send back an ack with an id
                #ack = f"ACK{ackNum}!"
                message = f"{c.getpeername()}> {message}"
                c.send(bytes(message, 'utf-8'))


#main server loop
while True:

    #accepts one connection for testing purposes
    if numConnection != 2:
        client, addr = server_socket.accept()
        numConnection +=1
        print(f"[*] New connection from {addr[0]}:{addr[1]}")
        clients.append(client)

        handleClientThread = threading.Thread(target=handleClient, args=(client,))
        handleClientThread.start()

    # #recieve message from client
    # message = client.recv(1024).decode('utf-8')
    # print(message)

    # for c in clients:
    #     if c != client:
    #         #send back an ack with an id
    #         ack = f"ACK{ackNum}!"
    #         client.send(bytes(ack, 'utf-8'))
    #         ackNum += 1