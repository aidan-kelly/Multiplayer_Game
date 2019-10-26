#!/usr/bin/env python3
from tkinter import *
import sys
import socket
import threading

###
### TODO Need to store user's name somewhere and also send to server
###      

#vars for width and height.
HEIGHT = 700
WIDTH = 1000

NAME = ""

#basic socket setup
TARGET_IP = '127.0.0.1'
TARGET_PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TARGET_IP, TARGET_PORT))

#set up our base window
root=Tk()
root.title("Chatroom")
root.geometry(f"{WIDTH}x{HEIGHT}")

#set up the console window
textbox=Text(root, bg='#080808', fg='#00BF20')
textbox.pack(fill=BOTH, expand=True)

#set up the input field
ourInput = Entry(root)
ourInput.pack(fill=X, side=BOTTOM)
ourInput.focus_set()

#create a seperate thread that will receive data
def receiveDataThread(client_socket):
    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        print(msg)

#This function will send off data
def returnPressed(event):

    global NAME

    #user hasn't set his username
    if NAME == "":
        NAME = ourInput.get()

        #clear the input field
        ourInput.delete(0, END)
        client_socket.send(bytes(f"NAME~{NAME}",'utf-8'))

        #spawn new thread to receive data from server
        receiveThread = threading.Thread(target=receiveDataThread, daemon=True, args=(client_socket,))
        receiveThread.start()

    else:

        #grab the input
        enterdText = ourInput.get()

        #check to see if user wants to exit
        if enterdText == "exit":
            client_socket.close()
            sys.exit()
        
        #output the text
        print(f"YOU> {enterdText}")

        #send the data to the server
        client_socket.send(bytes(enterdText, 'utf-8'))

        ###
        ### TODO in future, need to check this data before we send it to the server
        ###

        #ensure that the last entry in client is shown
        textbox.see("end")

        #clear the input field
        ourInput.delete(0, END)
        

#makes it so data is sent on pressing of RETURN key
root.bind("<Return>", returnPressed)

#makes it so that any print statements are printed to the textbox
def redirector(inputStr):
    textbox.insert(INSERT, inputStr)

#on print inserts data to text box
sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.

print("Please enter your username: ")

#start up the GUI
root.mainloop()