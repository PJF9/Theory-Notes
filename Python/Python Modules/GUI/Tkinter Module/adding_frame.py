from tkinter import *

root = Tk()

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=100, pady=100)

buuton = Button(frame, text='Whatever')
buuton.grid(row=0, column=0)

button_2 = Button(frame, text='OK')
button_2.grid(row=1, column=1)

# Can Do grid inside the Frame

root.mainloop()