from PyQt5 import QtWidgets
import sys


"""
- After importing some important modules we can create our
    main window

- Inside the window function first of all we need to create 
    the application object

- After that we need to create and modify the main window

- The last step is to show the window
"""

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    """
    1. The first argument is the x position of the window inside the monitor.
        ( 0,0 is the left up side of the screen and the positive is the right 
        and the down )
    
    2. The second argument is the y position of the window inside the modnitor
        ( those are the cordinates of the starting appearance of the window
        on the screen )

    3. The thirth argument is the width number

    4. The last argument is the height number
    """
    win.setGeometry(400, 150, 500, 500)
    win.setWindowTitle("This is the first window!")

    """
    Add some labels to the window
    - First we need to create the label object ( the parameter is where to put it )
    - Then we can create the text
    - Finally we have to place it one the window ( again with the cordinates )
        ( the parameters are the corinates )
    """
    label1 = QtWidgets.QLabel(win)
    label1.setText("Hallo There")
    label1.move(100, 300)

    label2 = QtWidgets.QLabel(win)
    label2.setText("Sir")
    label2.move(158, 300)

    win.show()
    """
    With this line by clicking the exit button at the window, the process is being
    more fluent
    """
    sys.exit(app.exec_())
    

window()