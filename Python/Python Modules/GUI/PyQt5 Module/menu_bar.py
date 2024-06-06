from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class My_Window(QtWidgets.QMainWindow):
    """
    This class is an exapmpe of a manu bar.
    The code is generated from the PyQt5 designer so the only
    think we do is to modify it and exmplain it
    """

    def __init__(self):
        """
        Because we have inherite the main window form the PyQt5
        module, the object of the class is going to be a window

        The first think we have to do is to call the 'parent'
        constructor, so we can use QMainWindow methods

        After that we can modify our window a little bit and call 
        the method that contains all the widgets 
        """

        super().__init__()

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Menu Bar")

        self.initUi()


    def initUi(self):
        """
        This method contain all the widgets that are placed on the
        main window

        To demonstrate the menu example we need to create a label.
        Althgough first we need to create the font object to set the
        font size bigger, so we can see

        After creating and modifuing the label object its time to 
        create the menubar object

        After creting the menubar object now we should create menu 
        title widgets and set the it one the screen.

        We can also create a status bar. This bar is at the lower side
        of the screen and prints a message if we hover down a button
        Again we have to set it on the screen

        After creating the menu titles we need to create the sub Actions
        to give our menu more functionality. Then we need to add them into
        the menu titles widjets. After all that we are ready to place them
        all into the menu.

        To give an example about what we can do with manus, we have created
        a method to change the labels text based on what menu button the
        user pushes.

        To connect the buttons with the method we need to call the triggered
        method on each one. At normal buttons we use the clicked. The defference
        is that with triggered we can activate the method via a keyboard
        shortcut.

        Because we want the function to take an argument as we passes the method
        in the connect method we need to create a lambda function. This is 
        nessessary becuase in other case we just passes the method's name,
        with a lambda function we can also pass the arguments  
        """

        #####################################################################
        font = QtGui.QFont()
        font.setPointSize(30)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test Label")
        self.label.setFont(font)
        self.label.adjustSize()
        self.label.move(135, 80)

        #####################################################################

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuExit = QtWidgets.QMenu(self.menubar)

        self.menuFile.setTitle("File")
        self.menuEdit.setTitle("Edit")
        self.menuSettings.setTitle("Settings")
        self.menuExit.setTitle("Exit")

        self.setMenuBar(self.menubar)

        #####################################################################

        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        #####################################################################

        self.menu_file_new = QtWidgets.QAction(self)
        self.menu_file_open = QtWidgets.QAction(self)
        self.menu_edit_copy = QtWidgets.QAction(self)
        self.menu_edit_paste = QtWidgets.QAction(self)
        self.menu_settings_preferences = QtWidgets.QAction(self)
        self.menu_confirm_exit = QtWidgets.QAction(self)

        self.menu_file_new.setText("New")
        self.menu_file_new.setStatusTip("Create a new file")
        self.menu_file_new.setShortcut("Ctrl+N")
        self.menu_file_open.setText("Open")
        self.menu_file_open.setStatusTip("Open a file")
        self.menu_file_open.setShortcut("Ctrl+O")
        self.menu_edit_copy.setText("Copy")
        self.menu_edit_copy.setStatusTip("Copy data")
        self.menu_edit_copy.setShortcut("Ctrl+C")
        self.menu_edit_paste.setText("Paste")
        self.menu_edit_paste.setStatusTip("Paste copied data")
        self.menu_edit_paste.setShortcut("Ctrl+V")
        self.menu_settings_preferences.setText("Preferences")
        self.menu_settings_preferences.setStatusTip("Open settings")

        self.menuFile.addAction(self.menu_file_new)
        self.menuFile.addAction(self.menu_file_open)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.menu_edit_copy)
        self.menuEdit.addAction(self.menu_edit_paste)
        self.menuEdit.addSeparator()
        self.menuSettings.addAction(self.menu_settings_preferences)
        self.menuSettings.addSeparator()
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        
        #####################################################################
        """
        With this way we can build a menu inside the menu
        """

        self.sub = self.menuExit.addMenu("Confirm Exit")
        self.ok_action = QtWidgets.QAction("Yes", self)
        self.no_action = QtWidgets.QAction("No", self)
        self.sub.addAction(self.ok_action)
        self.sub.addAction(self.no_action)

        #####################################################################

        self.menu_file_new.triggered.connect(lambda: self.clicked("A new file has created"))
        self.menu_file_open.triggered.connect(lambda: self.clicked("A file has opened"))
        self.menu_edit_copy.triggered.connect(lambda: self.clicked("Some data have copied"))
        self.menu_edit_paste.triggered.connect(lambda: self.clicked("Some data have pasted"))
        self.menu_settings_preferences.triggered.connect(lambda: self.clicked("Settings have opened"))
        self.ok_action.triggered.connect(lambda: self.clicked("Ok Pressed"))
        self.no_action.triggered.connect(lambda: self.clicked("No Pressed"))


    def clicked(self, text):
        """
        With this method we change the text label and abjust
        the new label size.
        We have created this method to demonstrate the menu
        functionality and the variaty of use that provides
        """

        self.label.setText(str(text))
        self.label.adjustSize()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    win = My_Window()

    win.show()
    sys.exit(app.exec_())
