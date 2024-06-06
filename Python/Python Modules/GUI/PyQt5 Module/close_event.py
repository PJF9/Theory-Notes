from PyQt5 import QtWidgets


class My_Window(QtWidgets.QMainWindow):
    """
    This class is helps us understand the CloseEvent
    method. This method is the method that is going to 
    be active when the user press the exit button of the
    screen.
    """

    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        self.show()


    def closeEvent(self, event):
        self.message_box = QtWidgets.QMessageBox.question(self, "Close Window",
            "Are you sure you want to close the window?", QtWidgets.QMessageBox.Yes 
            | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if self.message_box == QtWidgets.QMessageBox.Yes:
            event.accept()
            print("Closed")
        else:
            event.ignore()
            print("Not Closed")


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())
