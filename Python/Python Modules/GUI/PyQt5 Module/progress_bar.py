from PyQt5 import QtWidgets, QtCore


class My_Window(QtWidgets.QMainWindow):
    """
    This class is being made to demobstrate a progress bar
    example.
    """

    def __init__(self):
        """
        As with every program, the class object is going to
        be a main window, thus we need to inherite from the 
        PyQt5 module the QMainWindow class. Then we need to
        call the 'parent' constructor and after that we can
        use all the methods that is defined on the QMainWindow
        class to modify out object. At the end we need to call
        the initUI() method and show the window on the screen
        """

        super().__init__()

        self.setGeometry(440, 350, 400, 100)
        self.setWindowTitle("A basic progress bar")
        self.initUI()

        self.show()


    def initUI(self):
        """
        This method creates all the widgets that will be placed
        on the main window. To create a progress bar we need to
        use the QtWidgets.QProgressBar() method. After that to
        make the progress bar more functionable we need to 
        create a QtCore.QBasicTimer() object and a steping 
        variable 
        """

        self.progerss_bar_demo = QtWidgets.QProgressBar(self)
        self.progerss_bar_demo.setGeometry(40, 20, 350, 30)

        self.start_stop_button = QtWidgets.QPushButton(self)
        self.start_stop_button.setText("Start")
        self.start_stop_button.move(60, 65)
        self.start_stop_button.clicked.connect(self.start_prodress_bar)

        self.reset_button = QtWidgets.QPushButton(self)
        self.reset_button.setText("Reset")
        self.reset_button.move(232, 65)
        self.reset_button.clicked.connect(self.reset_progress_bar)

        self.timer = QtCore.QBasicTimer()
        self.step = 0


    def start_prodress_bar(self):
        """
        This method is the method that will be activated when we
        press the start/stop button. This item will stop the timer
        if we have pressed it one and it will create the timer
        start with the argument we passed it ( this argument is 
        the 'to' counter )
        """

        if self.timer.isActive():
            self.timer.stop()
            self.start_stop_button.setText("Start")
        else:
            self.timer.start(100, self)
            self.start_stop_button.setText("Stop")


    def reset_progress_bar(self):
        """
        This method is the method that will be activated when the user
        presses the reset button. This method set the progress bar value
        equal to 0 and stops the timer
        """

        self.step = 0
        self.progerss_bar_demo.setValue(0)
        self.timer.stop()

        self.start_stop_button.setText("Start")


    def timerEvent(self, event):
        """
        This method is the method that is always running. This method
        updates the progress bar value. The name must be the exact same 
        or else the progress bar will be static
        """

        if self.step >= 100:
            self.timer.stop()
            self.start_stop_button.setText("Start")
            self.step = 0
            return

        self.step += 1
        self.progerss_bar_demo.setValue(self.step)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = My_Window()

    sys.exit(app.exec_())