from tkinter import *

root = Tk()

def my_click():
    label = Label(root, text='I clicked the buttom')
    label.pack()

# With state i am determing what buttom will do
buttom_1 = Button(root, text='Click me', state=DISABLED) # We dont need the () cause it we
buttom_2 = Button(root, text='Click me', padx=50, pady=50, command=my_click, fg='blue', bg='black') # call the function instantly
buttom_2.pack()

root.mainloop()
