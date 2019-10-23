import socket
import random

TARGET_IP = '127.0.0.1'
TARGET_PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((TARGET_IP, TARGET_PORT))

while True:
    message = client_socket.recv(1024).decode('utf-8')
    if message == 'REQ':
        ourString = str(random.randint(1,100))
        client_socket.send(bytes(ourString, 'utf-8'))
        print(f"Sent out {ourString}")


    else:
        print(message)