from tkinter import *


window = Tk()

def left_click(event):
    print('Left')

def right_click(event):
    print('Right')

def middle_click(event):
    print('Middle')

# Window in window
frame = Frame(window, width=300, height=250)
frame.bind('<Button-1>', left_click)
frame.bind('<Button-2>', middle_click) # Scroll weel is Button 2
frame.bind('<Button-3>', right_click) # Right click is Button 3

# Dispaly on the screen
frame.pack()

window.mainloop()