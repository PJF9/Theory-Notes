from PyQt5 import QtWidgets, QtGui


class My_Window(QtWidgets.QMainWindow):
    """
    This class is an implemetning of the dial widget
    with PyQt5
    """

    def __init__(self):
        """
        Because we wnat the class to create a window
        object, we need to inherite from the QMainWindow
        class to modify our window. After calling the 
        'parent' constructor and modyfiyng the window 
        object we create a dial object and a label to 
        demonstrate or example
        """

        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Dial Example")

        self.dial = QtWidgets.QDial(self)
        self.dial.resize(150, 200)
        self.dial.setMaximum(100)
        self.dial.setMinimum(0)
        self.dial.setValue(33)
        self.dial.valueChanged.connect(lambda: self.label.setText(f"Dial Value: {self.dial.value()}"))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label = QtWidgets.QLabel(f"Dial Value: {self.dial.value()}", self)
        self.label.setFont(font)
        self.label.resize(100, 100)
        self.label.move(170, 20)

        self.show()


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())