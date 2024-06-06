from tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=100)
canvas.pack()

# By default its always black
black_line = canvas.create_line(0, 0, 200, 50) # First 2 for X and the other 2 for Y
red_line = canvas.create_line(0, 100, 200, 50, fill='red')

# First we have to give the point of the top left angle
# The next its the width and the height of the ractangel
green_bos = canvas.create_rectangle(25, 25, 150, 60, fill='yellow')

# Delete something
canvas.delete(red_line)
# Delete all
# canvas.delete(ALL)


window.mainloop()


