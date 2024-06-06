from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('350x285')

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

my_img = ImageTk.PhotoImage(Image.open('c:\\Users\\user\\OneDrive\\Έγγραφα\\Visual Studio 2019\\Python\\Tkinter\\2\\icon1.jpg'))
my_label = Label(frame, image=my_img)
my_label.place(relwidth=1, relheight=1)


root.mainloop()