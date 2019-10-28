#!/usr/bin/env python3
import socket
import threading

#basic socket setup
OUR_IP = '127.0.0.1'
OUR_PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((OUR_IP, OUR_PORT))
server_socket.listen(5)

#dictionary to map addresses to usernames
ADDRESS_TO_NAME = {}
CLIENTS = []

print(f"[*] Listening on {OUR_IP}:{OUR_PORT}")


#this function sends a message to all connections
def broadcast(client_socket, message):

    #see if the message is from the server
    if(client_socket == 'SERVER'):

        #if so send to all connected clients
        for c in CLIENTS:
            if c.getpeername() in ADDRESS_TO_NAME:
                c.send(bytes(message, 'utf-8'))

    #check if message is from connection
    else:

        #send to all connections that are not the sender
        for c in CLIENTS:
            if c.getpeername() != client_socket.getpeername():
                messageToSend = f"{ADDRESS_TO_NAME[client_socket.getpeername()]}> " + message
                c.send(bytes(messageToSend, 'utf-8'))


#function to send and receive data to client
def handleClient(client_socket):
    while True:

        #receive a message
        try:
            message = ""
            message = client_socket.recv(1024).decode('utf-8')
            print(message)

        #if a client leaves
        except ConnectionResetError:

            #remove the clients from our lists and inform the other connections
            print(f"[-] Connection closed from {client_socket.getpeername()}")
            CLIENTS.remove(client_socket)
            broadcast("SERVER", f"SERVER> {ADDRESS_TO_NAME[client_socket.getpeername()]} has left the chat.")
            ADDRESS_TO_NAME.pop(client_socket.getpeername(), None)
            return

        #checks for format of message. 
        tester = message.split('~')

        #see if we were sent a username
        if(tester[0] == 'NAME'):
            ADDRESS_TO_NAME[client_socket.getpeername()] = tester[1]
            broadcast("SERVER", f"SERVER> {tester[1]} joined the chat.")
            
        #if not, broadcast the message
        else:
            broadcast(client_socket, message)


#main server loop
while True:

    #accepts one connection for testing purposes
    client, addr = server_socket.accept()
    print(f"[*] New connection from {addr[0]}:{addr[1]}")
    CLIENTS.append(client)

    #spawn new thread to handle client
    handleClientThread = threading.Thread(target=handleClient, args=(client,))
    handleClientThread.start()