from PyQt5 import QtGui, QtWidgets


class My_Window(QtWidgets.QMainWindow):
    """
    This class is being made to understand combo boxes
    """

    def __init__(self):
        """
        Our class object will be a window object. To do that
        we need to inherite the QMainWindow class from the 
        PyQt5 module. To use all the QMainWindow class methods
        we need to call the 'parent' constructor. After that we 
        can use all the QMainWindow methods to modify our window
        At least we need to call the initUI() method. This method
        contains all the widgets that will be on our main window
        """

        super().__init__()

        self.setGeometry(100, 100, 581, 343)
        self.setWindowTitle("Combo Boxes Example")

        self.initUI()


    def initUI(self):
        """
        As we discuss earlier this method is going to contain all
        the widgets that will be placed on the main window

        First of all we need to change the font size of all the 
        widgets text

        Then it's time to create our combo boxes and modify them
        To add items inside the combo box we have two ways:
            1. Just use the addItem(text) method ( this method is
                going to pass an index to all the items based on the 
                order we type them in code, first will be 0, second 
                will be 1 ... )

            2. Just use the addItem("") method with empty text. After
                that use the setItemText(index, new_text) to modify
                the item's text

        By default the item that is going to appear on the combo box will
        be the item with index position 0. To change that we need to call
        the setCurrentText(text) or the setCurrentIndex(index) method.
        The item with the exact text will be the item that will appear and
        the same with the index

        After creating the combo boxes it's time to create a button and a 
        label, to demonstrate the combo boxes example.
        """

        font = QtGui.QFont()
        font.setPointSize(14)
        lebel_font = QtGui.QFont()
        lebel_font.setPointSize(20)

        self.comboX = QtWidgets.QComboBox(self)
        self.comboX.setGeometry(10, 10, 91, 31)
        self.comboX.setFont(font)
        self.comboX.addItem("0")
        self.comboX.addItem("1")

        self.comboY = QtWidgets.QComboBox(self)
        self.comboY.setGeometry(480, 10, 91, 31)
        self.comboY.setFont(font)
        self.comboY.addItem("")
        self.comboY.addItem("")
        self.comboY.setItemText(0, "0")
        self.comboY.setItemText(1, "1")
        
        self.submit = QtWidgets.QPushButton(self)
        self.submit.setGeometry(210, 240, 161, 51)
        self.submit.setFont(font)
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.pressed)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(147, 60, 381, 131)
        self.label.setFont(lebel_font)
        self.label.setText("Press Submit to find XOR")

    
    def pressed(self):
        """
        This method is the method that will be called when the 
        user press the submit button. The only think that this
        method does is to find the xor between the combo boxes
        items. To get the items from the combo box we need to 
        use the currentText() method. This gives us the text
        of the item that is currently on. After calculating the
        xor, we change the label's text with the result and we 
        move the label a little to the right
        """

        x = int(self.comboX.currentText())
        y = int(self.comboY.currentText())

        xor = (x and not y) or (not x and y)
        xor = 1 if xor == True else 0

        self.label.setText(f"X XOR Y = {str(xor)}")
        self.label.setGeometry(217, 60, 381, 131)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = My_Window()
    
    win.show()
    sys.exit(app.exec_())
