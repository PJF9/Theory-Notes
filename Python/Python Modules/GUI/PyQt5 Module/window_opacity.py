from PyQt5 import QtWidgets
from sys import argv, exit


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    
    win = QtWidgets.QMainWindow()
    win.resize(300, 200)

    button = QtWidgets.QPushButton("Button", win)
    button.move(95, 70)

    """
    What is window opacity?
    This how dense will the widow look.
    By default is 1 (100%).
    But we can change that.
    Only flaoting point values are allowed.
    Floating numbers between 0-1

    By changing the opasity we are chaning all the 
    widget's opasity
    """

    win.setWindowOpacity(0.95)

    win.show()
    exit(app.exec_())