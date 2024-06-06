from tkinter import *

root = Tk()
root.geometry("200x200")

menu = Menu(root, tearoff=0)
root.config(menu=menu)

class App:
    def __init__(self, master, i_menu):
        self.matser = master
        self.i_menu = i_menu

        self.file_menu = Menu(self.i_menu, tearoff=0)
        self.i_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.print_hi)

        self.edit_menu = Menu(self.i_menu, tearoff=0)
        self.i_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Copy", command=NONE)

        self.show_menu = Menu(self.i_menu, tearoff=0)
        self.i_menu.add_cascade(label="Show", menu=self.show_menu)
        self.show_menu.add_command(label="Show", command=NONE)

        self.exit_menu = Menu(self.i_menu, tearoff=0)
        self.i_menu.add_cascade(label="Exit", menu=self.exit_menu)
        self.exit_menu.add_command(label="Exit", command=master.destroy)


    def print_hi(self):
        Label(text="HI").pack()

App(root, menu)

root.mainloop()