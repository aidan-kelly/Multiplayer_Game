import socket
import time

OUR_IP = '127.0.0.1'
OUR_PORT = 1234
CLIENT_LIST = []

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind((OUR_IP, OUR_PORT))
server_sock.listen(5)

print(f"[*] Listening on {OUR_IP}:{OUR_PORT}")

while True:
    #waiting on our two players
    if len(CLIENT_LIST) != 2:
        client, addr = server_sock.accept()
        
        #.peername() is the address of the socket
        print(client.getpeername())
        CLIENT_LIST.append(client)

    #we now can relay the messages
    else:
        print("OH BOY WE HAVE A LOT OF CONNECTIONS.")
        
        while True:
            time.sleep(2)

            #loop through our clients
            for client in CLIENT_LIST:
                client.send(bytes("REQ", "utf-8"))

            time.sleep(1)

            for client in CLIENT_LIST:
                us = client.getpeername()
                message = str(us) + " sends: "

                ###
                ### FOR SOME REASON WE ARENT GETTING DATA HERE SOMETIMES
                ### MIGHT HAVE BEEN A RACE CONDITION OF SOME KIND REVOLVING AROUND THE REQ MESSAGE
                ### WOULD SEND OUT 29REQ MESSAGES
                ###
                message += client.recv(1024).decode("utf-8")

                print(message)

                for client in CLIENT_LIST:
                    if client.getpeername != us:
                        client.send(bytes(message, 'utf-8'))
