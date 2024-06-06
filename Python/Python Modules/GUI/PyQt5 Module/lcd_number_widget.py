from PyQt5 import QtWidgets, QtCore


class My_Window(QtWidgets.QMainWindow):
    """
    This class is demonstrating an example with the
    LCD number and the slider objects
    """

    def __init__(self):
        """
        This class is going to create a window object,
        thus we need to inherite from the QMainWinodw
        class so we can use the main window methods
        """

        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle("LCD example")
        self.initUI()

        self.show()
    
    
    def initUI(self):
        """
        This method is creating all the widgets that we will
        need to demonstrate the example. We will need a lcd
        and a slider objects. By default the slider has
        vertical orientation, so to change that we need to
        call the setOrientation() method. Then we can play
        with the maximum and the minimum values. The value
        that the slider will have at the start is 0 and the 
        max is 99 ( min is -99 ). To change the LCD number
        object we need to call the valueChanger() method to 
        the slider 
        """

        self.lcd = QtWidgets.QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 400, 269)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setGeometry(1, 270, 399, 30)
        self.slider.setMaximum(99)
        self.slider.setMinimum(-99)
        self.slider.valueChanged.connect(self.updateLCD)


    def updateLCD(self, event):
        """
        This method is changing the value of the LCD number
        """

        self.lcd.display(event)


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())
