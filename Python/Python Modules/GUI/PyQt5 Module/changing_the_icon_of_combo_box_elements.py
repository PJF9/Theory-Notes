from PyQt5 import QtWidgets, QtGui
from sys import argv, exit


"""
This is the way to add an icon left to a combo box
object
"""

app = QtWidgets.QApplication(argv)

win = QtWidgets.QMainWindow()
win.setWindowTitle("Combo Example")
win.resize(200, 150)

combo = QtWidgets.QComboBox(win)
combo.move(50, 50)

combo.addItem(QtGui.QIcon("C:\\Users\\jacob\\Photos\\1.jpg"), "Yes")
combo.addItem(QtGui.QIcon("C:\\Users\\jacob\\Photos\\2.jpg"), "No")

win.show()
exit(app.exec_())