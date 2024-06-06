from tkinter import *


def do_nothing():
    print('Ok')


window = Tk()
window.geometry("300x300")

# --------- Menu Drop Down --------#
menu = Menu(window)
window.config(menu=menu) # We need to config the menu

sub_menu = Menu(menu)
# Drop out functionality
menu.add_cascade(label='File', menu=sub_menu)

sub_menu.add_command(label='New Project...', command=do_nothing)
sub_menu.add_command(label='New...', command=do_nothing)
# Create the line to separate the items
sub_menu.add_separator()
sub_menu.add_command(label='Ext...', command=do_nothing)

# New menu item
edit_menu = Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', command=do_nothing)
# --------- Menu Drop Down --------#

# ----- Toolbar Making ------------# 
toolbar = Frame(window, bg='blue')
insert_buttom = Button(toolbar, text='Isner image', command=do_nothing)
insert_buttom.pack(side=LEFT, padx=2, pady=2)

print_buttom = Button(toolbar, text='Print', command=do_nothing)
print_buttom.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)
# ----- Toolbar Making ------------# 

# ------ Status Bar ---------------#
status = Label(window, text='Preparing to do nothing', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
# ------ Status Bar ---------------#


window.mainloop()