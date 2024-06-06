from PyQt5 import QtWidgets, QtGui


class My_Window(QtWidgets.QMainWindow):
    """
    This class is going to help us create a dock widget. This 
    widget is a sub window in the main window that we can extract
    it from the main one. Inside this window we will create a list
    widgets and store some companies names. After clicking the text
    twice the name the text will appear on the text editor
    """

    def __init__(self):
        """
        Of course this class is going to create a main window
        so we need to inherite from the QMainWindow class to 
        use all the methods we want to modify our window
        """

        super().__init__()

        self.resize(800, 500)
        self.setWindowTitle("Dock Widget example")
        self.initUI()

        self.show()
        
    
    def initUI(self):
        """
        This method is going to create all the widgets we need to
        demonstrate the dock example. Wew create a dock widget, a 
        text editor, a list widget, a label and a button objects.
        To change the text editor text we need to click twice the 
        item inside the list widget. To get the functionality we 
        need to call the itemDoubleClicked() method
        """

        self.dock_widget = QtWidgets.QDockWidget("Companies", self)
        self.dock_widget.setGeometry(500, 0, 300, 500)

        self.text_editor = QtWidgets.QTextEdit(self)
        self.text_editor.setFontPointSize(14)
        self.text_editor.setGeometry(0, 0, 500, 500)

        self.list_widget = QtWidgets.QListWidget(self.dock_widget)
        self.list_widget.setGeometry(75, 25, 150, 100)
        self.list_widget.addItem("Microsoft")
        self.list_widget.addItem("Apple")
        self.list_widget.addItem("IBM")
        self.list_widget.addItem("Facebook")
        self.list_widget.itemDoubleClicked.connect(self.get_dock_item)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.label = QtWidgets.QLabel("Some Additions", self.dock_widget)
        self.label.setFont(font)
        self.label.adjustSize()
        self.label.move(85, 400)

        font.setPointSize(12)
        self.button = QtWidgets.QPushButton("Display", self.dock_widget)
        self.button.setFont(font)
        self.button.move(90, 450)
        self.button.setShortcut("Ctrl+S")
        self.button.clicked.connect(self.change_label_text)


    def get_dock_item(self):
        """
        This mehtod changes the text editor's text
        """

        self.text_editor.setPlainText(self.list_widget.currentItem().text())


    def change_label_text(self):
        """
        This method changes the label's text.
        With toPlainText() we get the text of the text editor object
        """

        self.label.setText(self.text_editor.toPlainText())
        self.label.adjustSize()


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())
