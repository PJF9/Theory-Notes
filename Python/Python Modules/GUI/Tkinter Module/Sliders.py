from tkinter import *

root = Tk()
# Setting up the size
# root.geometry('500x500')

def slide(var):
    Label(root, text=vertical.get()).pack()
    root.geometry(f'380x{vertical.get()}')

vertical = Scale(root, from_=200, to=800, command=slide)
vertical.pack()

horizontal = Scale(root, from_=0, to=300, orient=HORIZONTAL)
horizontal.pack()

Button(root, text='Ok', command=slide).pack()

root.mainloop()