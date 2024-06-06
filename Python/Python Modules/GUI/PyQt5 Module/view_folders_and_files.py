from PyQt5 import QtWidgets, QtCore


class My_Window(QtWidgets.QMainWindow):
    """
    This class is going to create a window that will
    display all the files and folder of a specific path
    """

    def __init__(self, dir_path):
        """
        This class is going to create a window object,
        thus we need to inherite from the QMainWindow
        class so we can use all the main window method
        to modify our own one.

        Then we need to create a file system model ( this
        is the object that will copy the file system view
        so we can display the path like this ).

        After that we need to create a tree view object to
        display the file model object. After pass the self 
        argument, so the tree view object will display on
        the main window we need to add the file system model
        with the setModel() method.

        Then if we want the tree view to show the specific path
        we need to call the setRootIndex() method with argument
        model.index(path). Else we displaying the c:/ directory

        To make the tree view object prettier we resize it and
        setting the column width bigger. At least we add the 
        setAlternativeRowColors(True) method 
        """

        super().__init__()

        self.resize(600, 500)
        self.setWindowTitle("View folders and files")

        self.model = QtWidgets.QFileSystemModel(self)
        self.model.setRootPath(dir_path)

        self.tree_view = QtWidgets.QTreeView(self)
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(dir_path))
        self.tree_view.resize(600, 500)
        self.tree_view.setColumnWidth(0, 250)
        self.tree_view.setAlternatingRowColors(True)

        self.show()


if __name__ == "__main__":
    from sys import argv, exit

    app = QtWidgets.QApplication(argv)

    path = r"C:\USB\Programming\Python\Modules"
    win = My_Window(path)

    exit(app.exec_())