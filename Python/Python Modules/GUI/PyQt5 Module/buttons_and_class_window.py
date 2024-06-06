from PyQt5 import QtWidgets
import sys


class My_Window(QtWidgets.QMainWindow):
    """
    This is the window class. This class is ordering the
    code in a more readable way

    ...


    Inheritance
    -----------
    QtWidgets.QMainWindow:
        This is the Qt5 main window. We inherite from it so
        we can use all the Qt5 window methods, such as the 
        setGeometry() and the setWindowTitle() 
    """
    
    def __init__(self):
        """
        To use all the methods from the QMainWidget class we
        need to class the 'parent' constructor
        -
        After that we can use all the methods we need to modify
        our window
        -
        Then we need to call the initUI method ( the method that
        contains all the widgets )
        """
        
        super().__init__()

        self.setGeometry(400, 200, 500, 500)
        self.setWindowTitle("This is a class made app")
        self.initUI()


    def initUI(self):
        """
        This method will contain all the widget that will be 
        placed on the screen.
        -
        This method we are going to call it on the initializer
        -
        As the 'where to put it' parameter we need to pass
        self, because self is the window object
        """

        self.label = QtWidgets.QLabel(self)
        self.label.setText("This is a pretty label")
        self.label.move(200, 200)

        """
        Now its time to create a button. To make the button more 
        functional we can create a function ( method ) when we
        press the button this funtcion ( method ) will activate.
        The last line of this method is the connection between the
        on_click() method with the button
        """

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("This is a pretty button")
        self.button.move(100, 100)
        self.button.adjustSize()
        self.button.clicked.connect(self.on_click)


    def on_click(self):
        """
        After changing the label's text we have to modify the size
        of the label. It doesn't changes the size by itself so we
        need to call the adjustSize() method
        """

        self.label.setText("The label text change")
        self.label.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = My_Window()

    win.show()
    sys.exit(app.exec_())
