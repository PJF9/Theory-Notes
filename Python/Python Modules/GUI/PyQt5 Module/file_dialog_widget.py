from PyQt5 import QtWidgets, QtGui, QtCore


class My_Window(QtWidgets.QMainWindow):
    """
    This class is being made to create and use the PyQt5
    file dialog class
    """

    def __init__(self):
        """
        As with every application the object that this class
        is going to create is a window object. Thus we need 
        to inherite from the QMainWindow class. After calling
        the 'parent' constructor and modifying out own window
        we call the iniUI() class and then we show the window
        on the screen
        """

        super().__init__()

        self.resize(1000, 600)
        self.setWindowTitle("File Dialog Example")
        self.initUI()

        self.show()


    def initUI(self):
        """
        This class is creating all the widgets that will be placed
        on the main window. First off all we create a font object 
        so we can change the font off every widget. After that we
        create two buttons to help us with the application. Finishing
        with the widgets we create a label and a text editor objects
        """

        font = QtGui.QFont()
        font.setPointSize(11)

        self.button1 = QtWidgets.QPushButton("Upload image", self)
        self.button1.resize(1000, 30)
        self.button1.setFont(font)
        self.button1.clicked.connect(self.get_image_file)

        self.button2 = QtWidgets.QPushButton("Upload python file", self)
        self.button2.resize(1000, 30)
        self.button2.move(0, 400)
        self.button2.setFont(font)
        self.button2.clicked.connect(self.get_python_file)

        self.photo_label = QtWidgets.QLabel(self)
        self.photo_label.setGeometry(0, 31, 1000, 369)
        
        self.text_editor = QtWidgets.QTextEdit(self)
        self.text_editor.setGeometry(0, 431, 1000, 169)


    def get_image_file(self):
        """
        This method opens the file dialog and helps us demonstrate the 
        example. The getOpenFileName() method takes four arguments:
            1. The placeholder
            2. The title of the window
            3. The path we want to default open
            4. The specific files we want ('Image File' is the title so
                we can skip it, the actual argument is the (...))
        
        At least to past the icon file on the screen we assign it to the
        photo label
        """

        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image File", r"C:\\Users\\jacob\\Photos", "Image Files (*.png *.jpg *.gif)")
        self.photo_label.setPixmap(QtGui.QPixmap(file_name))


    def get_python_file(self):
        """
        This method does the same job as the previews method with the 
        deffernet that we can see the code off every python file in 
        the text editor object. The dialog.exec_() condition is True
        when we press the open with the file manager. file_name is
        a list that has only one element: the complete path of the
        file we clicked ( including the name ). With the file.read()
        method we get all the text from the python file.
        """

        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle("Open Python File")

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith(".py"):
                with open(file_name[0], "r") as file:
                    data = file.read()
                    self.text_editor.setPlainText(data)


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())