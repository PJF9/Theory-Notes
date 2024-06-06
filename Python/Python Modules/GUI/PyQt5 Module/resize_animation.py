from PyQt5 import QtWidgets, QtCore


class My_Window(QtWidgets.QMainWindow):
    """
    This class is resizing the main window with a pretty
    animation.
    """

    def __init__(self):
        """
        The object that this class we want to create is a
        window object. Thus we need to inherite from the 
        QMainWindow class, so to use all the methods to
        modify our window. After that we need to create 
        the starting width and height pixels to modify
        them later.
        """

        super().__init__()

        self.base_height = 50
        self.extend_height = 300

        self.base_width = 120
        self.extend_width = 400

        self.setGeometry(520, 200, self.base_width, self.base_height)
        self.setWindowTitle("Resizing Animation")

        self.button = QtWidgets.QPushButton("Expand", self)
        self.button.clicked.connect(self.resize_window)

        self.show()


    def resize_window(self):
        """
        This class is going to be called when we want to
        resize the window with a pretty animation.
        First of all we need to get the current window 
        size to compare it with the base one. If the current
        size is equal to the base one we will expand the size,
        else we will shrink it. After the condition we need to
        create the QPropertyAnimation object. The second parameter
        is the 'state of an animation' and we need to pass this
        terible thing. Then we can set the total time in miliseconts
        that it will take to expand/shring the size of the window.
        Then we have to decalre the starting and the ending window
        size and at least we need to call the start() method to 
        start the animation
        """

        current_height = self.height()
        current_width = self.width()

        if current_height == self.base_height:
            now_height, after_height = self.base_height, self.extend_height
            self.button.setText("Shrink")
        else:
            now_height, after_height = self.extend_height, self.base_height
            self.button.setText("Expand")

        if current_width == self.base_width:
            now_width, after_width = self.base_width, self.extend_width
        else:
            now_width, after_width = self.extend_width, self.base_width

        self.animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(800) # unit is on miliseconts 10^-2
        self.animation.setStartValue(QtCore.QRect(520, 200, now_width, now_height))
        self.animation.setEndValue(QtCore.QRect(520, 200, after_width, after_height))
        self.animation.start()


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)
    win = My_Window()

    exit(app.exec_())
