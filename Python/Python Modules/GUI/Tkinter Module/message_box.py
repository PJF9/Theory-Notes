from tkinter import *
from tkinter import messagebox

root = Tk()

# Defining the message popup function

def popup_1():
    response = messagebox.showinfo('This is a popup', 'Whatever')
    # If clicked ok respone = ok
    if response == 'ok':
        root.quit()


def popup_2():
    respone = messagebox.showwarning('This is a popup', 'Whatever')
    # If clicked ok respone = ok
    if respone == 'ok':
        root.quit()

def popup_3():
    respone = messagebox.showerror('This is a popup', 'Whatever')
    # If clicked ok response = ok
    if respone == 'ok':
        root.quit()


def popup_4():
    respone = messagebox.askquestion('This is a popup', 'Are you play ping pong?')
    # If clicked yes response = yes else no
    if respone == 'yes':
        Label(root, text='Nice, I play too').pack()
    elif respone == 'no':
        Label(root, text='Its fine, me neither').pack()


def popup_5():
    respone = messagebox.askokcancel('This is a popup', 'Whatever')
    # If clicked ok respone = 1 else 0
    if respone == 1:
        Label(root, text='You have clicked Ok').pack()
    elif respone == 0:
        root.quit()


def popup_6():
    respone = messagebox.askretrycancel('This is a popup', 'Whatever')
    # if click repeat response = 1 else 0
    if respone == 1:
        Label(root, text='You have clicked repeat').pack()
    elif respone == 0:
        root.quit()


def popup_7():
    response = messagebox.askyesno('This is a popup', 'Whatever')
    # If clicked yes respone = 1 else 0
    if response == 1:
        Label(root, text='You have clicked yes').pack()
    elif response == 0:
        Label(root, text='You have clicked no').pack()


# Creating the Button to call the message function
button = Button(root, text='This is a popup', command=popup_3)
# As always we need to pack this in screen
button.pack()


root.mainloop()