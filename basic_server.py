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

#function to send and receive data to client
def handleClient(client_socket):
    while True:
        message = ""
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
        for c in clients:
            if c.getpeername() != client_socket.getpeername():
                #send back an ack with an id
                #ack = f"ACK{ackNum}!"
                #message = f"{c.getpeername()}> {message}"

                ###
                ### TODO need to add the sender's name in from of message.
                ###      ex: <NAME>: Message goes here.
                ###

                c.send(bytes(message, 'utf-8'))


#main server loop
while True:

    #accepts one connection for testing purposes
    client, addr = server_socket.accept()
    numConnection +=1
    print(f"[*] New connection from {addr[0]}:{addr[1]}")
    clients.append(client)

    #spawn new thread to handle client
    handleClientThread = threading.Thread(target=handleClient, args=(client,))
    handleClientThread.start()