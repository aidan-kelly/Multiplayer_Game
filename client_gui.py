# import tkinter

# HEIGHT = 700
# WIDTH = 1000

# root = tkinter.Tk()
# root.title("Chatroom")
# root.geometry(f"{WIDTH}x{HEIGHT}")

# termf = tkinter.Frame(root, height=650, width=950)
# termf.grid(column=0, row=0)

# text = tkinter.Entry(root, width=WIDTH)
# text.grid(column=0, row=1)

# root.mainloop()

from tkinter import *
import sys

HEIGHT = 700
WIDTH = 1000

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

#This function will send off data
def func(event):

    #grab the input
    enterdText = ourInput.get()

    #check to see if user wants to exit
    if enterdText == "exit":
        sys.exit()
    
    #output the text
    print(enterdText)
    textbox.see("end")
    ourInput.delete(0, END)
    

#makes it so data is sent on pressing of RETURN key
root.bind("<Return>", func)

#makes it so that any print statements are printed to the textbox
def redirector(inputStr):
    textbox.insert(INSERT, inputStr)

#on print inserts data to text box
sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.

#start up the GUI
root.mainloop()