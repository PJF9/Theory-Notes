from tkinter import *

# Creating the root window
root = Tk()
root.title('Suppp')

# Define open the second window function
def open_wind():
    # Creating the second winsdow
    top = Toplevel()
    top.title('HI!!!')
    # Creating a label inside second window
    Label(top, text='Supppp').pack()

    # Making the button to call the function
    # If we call quit() then it will closed and the first window
    Button(top, text='Close Window', command=top.destroy).pack()


button = Button(root, text='Open secont window', command=open_wind)
button.pack()

root.mainloop()