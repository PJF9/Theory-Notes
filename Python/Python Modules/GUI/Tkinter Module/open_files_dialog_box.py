from tkinter import *
from tkinter import filedialog

root = Tk()

def Open():
    root.filename = filedialog.askopenfilename(initialdir='/User/user', title='Select a file', filetypes=(('all files', '*.*') ,('all files', '*.*')))
    # This return the location of the file

Button(root, text='Open', command=Open).pack()

root.mainloop()