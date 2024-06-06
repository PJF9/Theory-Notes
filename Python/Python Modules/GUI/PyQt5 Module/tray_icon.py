from PyQt5 import QtWidgets, QtGui
from sys import argv, exit

class My_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("C:\\Users\\jacob\\Photos\\1.png"), parent=self)
        self.trayIcon.setToolTip("Example py")
        self.trayIcon.show()

        self.resize(200, 200)
        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())
    