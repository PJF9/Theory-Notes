from tkinter import *


window = Tk()

label_1 = Label(window, text='Name')
label_2 = Label(window, text='Password')

# Entry = Input
entry_1 = Entry(window)
entry_2 = Entry(window)

# Its like pack but you can organise better the labels
label_1.grid(row=0, sticky=E) # By default the column is always equal to zero
label_2.grid(row=1, sticky=E)# Stick atands for putting W,E,N,S in the row

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

# Pace a little box for me to check or uncheck
c = Checkbutton(window, text='Keep me logged in')
c.grid(columnspan=2) # Place in the center of 2 columns

window.mainloop()