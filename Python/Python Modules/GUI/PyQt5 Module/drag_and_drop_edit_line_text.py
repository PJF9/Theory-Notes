from PyQt5 import QtWidgets


class My_Window(QtWidgets.QMainWindow):
    """
    This class is a basic example of the drag and drop
    effect between edit line text objects to other lines
    objects, buttons and labels
    """

    def __init__(self):
        """
        This class is going to create a window object. So
        we need to inherite from the QMainWindow class to
        modify our window object. Then we need to call the
        initUI() method and al least we need to show our 
        window
        """

        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Drag and Drop Effect")
        self.initUI()

        self.show()
        

    def initUI(self):
        """
        This method is the method that will create all the
        widgets that will be placed on the screen. We will
        create two edit line objects, one button object and 
        one label objects  
        """

        self.edit_1 = QtWidgets.QLineEdit("", self)
        self.edit_1.move(30, 20)
        self.edit_1.setDragEnabled(True)

        self.edit_2 = QtWidgets.QLineEdit("", self)
        self.edit_2.move(30, 100)
        self.edit_2.setDragEnabled(False)

        self.my_button = Button("Click", self)
        self.my_button.move(150, 30)

        self.label = Label("My", self)
        self.label.move(150, 60)


"""
To activate the drop effect to a button ore a label
we need to create our calsses to modify two methods
The methods we need to modify are the dropEnterEvent()
and the dropEvent()
"""

class Button(QtWidgets.QPushButton):
    def __init__(self, title, parent):
        """
        The parameters are the starting text and the window
        we want the button to be placed. After calling the
        'parent' constructor and then we need to call the 
        setAcceptDrops(True) method to start the drop effect
        """

        super().__init__(title, parent)
        self.setAcceptDrops(True)

    """
    Those methods are the reson we need to update the PyQt5
    PushButton class. With those classes we setting a new
    text at the widgest
    """
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())

"""
The same logic with the button applies for the label widget
"""
class Label(QtWidgets.QLabel):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())




if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())