from PyQt5 import QtWidgets


class My_Window(QtWidgets.QMainWindow):
    """
    This class is being made to better understands the message
    boxes
    """

    def __init__(self):
        """
        This class is inherite from the QMainWindow class inside
        the PyQt5 module. Thus we need to call the 'parent' constructor
        so we call all the window methods
        
        The object that our class will create is a window object
        
        After modifying out window object we call the iniUI() method.
        This method is creating all the widgets that will be placed
        on the screen
        """
        
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Pop up windows example")
        self.initUI()


    def initUI(self):
        """
        This method creates a basic button so when we press
        it we open the pop up window
        """

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Open Pop Up Window")
        self.button.adjustSize()
        self.button.setGeometry(135, 150, 130, 65)

        self.button.clicked.connect(self.open_popup)


    def open_popup(self):
        """
        This method is the method that will be activated when the 
        button is clicked

        This method creates a Message Box object and setting the 
        title and the text of it

        Then we change the icon that describes what the message box
        is oposed to do. Options:
            1. QtWidgets.QMessageBox.Information
            2. QtWidgets.QMessageBox.Quextion
            3. QtWidgets.QMessageBox.Warning
            4. QtWidgets.QMessageBox.Critical

        After that we could set some buttons to be displayed on the 
        window. Options:
            1. QtWidgets.QMessageBox.Cancel
            2. QtWidgets.QMessageBox.Retry
            3. QtWidgets.QMessageBox.Ignore
            4. QtWidgets.QMessageBox.Yes
            5. QtWidgets.QMessageBox.No
            6. QtWidgets.QMessageBox.Open
            7. QtWidgets.QMessageBox.Save
            8. QtWidgets.QMessageBox.Close
            9. QtWidgets.QMessageBox.Abort
            10. QtWidgets.QMessageBox.Ok

        Then we could set a secondary text that will go under the main 
        text

        Another option is set a detailed text. This will create a new button
        on the message box and when we press it it will create a drop canvas
        with the text of the argument

        As with the normal buttons with pop up buttons we can create a 
        mehtod to call it when we press a button. This method must take
        as an argument the button, so i is the button we press and then
        inside the method we can do whatever we want.

        Finally to place the Message Box on the window we need to call
        the exec_() method 
        """

        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("First Pop up Window")
        self.msg.setText("This is the popup text")
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Cancel|QtWidgets.QMessageBox.Retry|QtWidgets.QMessageBox.Ignore)
        self.msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
        self.msg.setInformativeText("Informative Text")
        
        self.msg.setDetailedText("Detailed Text")

        self.msg.buttonClicked.connect(self.pop_but_clicked)

        self.msg.exec_()


    def pop_but_clicked(self, i):
        print(i.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = My_Window()

    win.show()
    sys.exit(app.exec_())
