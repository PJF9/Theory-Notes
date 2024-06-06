from tkinter import *

root = Tk()
root.geometry('400x400')

def show():
    Label(root, text=var.get()).pack()
    Label(root, text=var1.get()).pack()
    
    if (var1.get() == 'on') and (var.get() == 'off'):
        print('1')
    elif (var1.get() == 'off') and (var.get() == 'on'):
        print('2')
    else:
        print('eafgAE')


var = StringVar()
# Now we have the variable string becasue we dont want 0 and 1, we want on anf off
c = Checkbutton(root, text='Ok', variable=var, onvalue='on', offvalue='off')
c.deselect()
c.pack()

var1 = StringVar()
c1 = Checkbutton(root, text='ok1', variable=var1, onvalue='on', offvalue='off')
c1.deselect()
c1.pack()


Button(root, text='Ok', command=show).pack()

root.mainloop()