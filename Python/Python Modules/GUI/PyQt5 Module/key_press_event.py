from PyQt5 import QtWidgets, QtGui, Qt


class My_Window(QtWidgets.QMainWindow):
    """
    This class is helping us understand how to use
    the ket press event method in our window
    """

    def __init__(self):
        """
        The object that our class we want to create is 
        a window object, thus we need to inherite from
        the QMainWindow class so we can use all the 
        main window methods to modify our window. After
        that we create a label object se we can see the 
        keys on the screen.
        """

        super().__init__()
        
        self.resize(300, 200)
        self.setWindowTitle("Key Press Example")

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(130, 40, 100, 100)
        self.label.setFont(font)

        self.show()


    def keyPressEvent(self, event):
        """
        This method is the method that is always runing
        and captioning the key strockes we press. The 
        naming must be the exact same or else the method
        will no run. With text() method we get the value
        of all the alpharithmitic letters and with the
        key() method we get the key of every key on the
        keyboard. At least to compare a key we use the
        Qt.Key_something key.
        """

        self.label.setText(str(event.text()))

        if event.key() == Qt.Qt.Key_Space:
            self.label.setText("Space")
        elif event.key() == Qt.Qt.Key_Backspace:
            self.label.setText("Back Space")


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())