from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='yellow', fg='red', borderwidth=8)
e.pack()
e.insert(0, 'Enter your Name: ')

def click():
    label = Label(root, text=f'Hello {e.get().split(":")[-1]}')
    label.pack()

buttom = Button(root, text='Enter your name', command=click)
buttom.pack()

root.mainloop()