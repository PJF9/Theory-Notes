from tkinter import *


root = Tk()

# r = IntVar()

Modes = [
    # Text # Mode
    ('1', 'ok'),
    ('2', 'Ok'),
    ('3', 'oK'),
    ('4', 'OK')
]

whatever = StringVar()

for text, mode in Modes:
    a = Radiobutton(root, text=text, variable=whatever, value=mode)
    a.pack(anchor=W)


def clicked(value):
    label = Label(root, text=value)
    label.pack()

# Or
# r = StringVar()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 1', variable=r, value=2, command=lambda: clicked(r.get())).pack()


# label = Label(root, text=whatever.get())
# label.pack()

button = Button(root, text='Ok', command=lambda: clicked(whatever.get()))
button.pack()

root.mainloop()
