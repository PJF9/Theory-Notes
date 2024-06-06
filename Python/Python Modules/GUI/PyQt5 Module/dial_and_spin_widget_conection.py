from PyQt5 import QtWidgets, QtGui


class My_Window(QtWidgets.QMainWindow):
    """
    Another example with dial widget. Might be usefull
    Line 27 and 28 are the crusial ones. These lines connect
    the spinbox object and the dial one.
    """

    def __init__(self):
        super().__init__()

        self.resize(300, 300)
        
        dial = QtWidgets.QDial(self)
        dial.setGeometry(70, 30, 150, 150)
        dial.setNotchesVisible(True)

        font = QtGui.QFont()
        font.setPointSize(12)

        spin = QtWidgets.QSpinBox(self)
        spin.setGeometry(126, 230, 50, 50)
        spin.setFont(font)

        dial.valueChanged.connect(spin.setValue)
        spin.valueChanged.connect(dial.setValue)

        self.show()


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())