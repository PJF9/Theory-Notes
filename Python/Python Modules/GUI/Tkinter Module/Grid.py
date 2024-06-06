from tkinter import *


root = Tk()

label_1 = Label(root, text='Hallo')
label_2 = Label(root, text='World')

label_1.grid(row=0, column=1)
label_2.grid(row=1, column=6)

root.mainloop()