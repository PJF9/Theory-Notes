from tkinter import *


# Create a class
class Petros_Buttons:
    
    # Class parameters
    def __init__(self, master):
        # We have rename window as master
        frame = Frame(master)
        frame.pack()

        # Creating the buttons
        self.print_button = Button(frame, text='Print Message', command=self.print_Message)
        self.print_button.pack(side=LEFT)
        self.quit_button = Button(frame, text='Quit Message', command=frame.quit)
        self.quit_button.pack(side=LEFT)

    # Crating the print message
    def print_Message(self):
        Label(window, text='Ok').pack()


window = Tk()
# Creating the object with the only parameter
Object = Petros_Buttons(window)

window.mainloop()