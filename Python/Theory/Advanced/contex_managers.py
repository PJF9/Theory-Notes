"""
Contex Manager is a Python's way to make our life a lot eazier when using files,
databases and other objects that first we need to connect to them.

The upside for using contex manager instead of the typical 'open()/close()' inside
a 'try/catch' statement is that is an unpredictable situation that our program will
crush, Python runs a method to close the file/database or in general the connection
we have opened.

The syntax we use is:
    with some_funct('some_name', 'mode') as alias:
        actions

Where 'some_funct' is the name of the function we use to establish some connection
"""

with open("numbers.txt", "w") as file:
    print(file.closed)
print(file.closed)



# Creating our own Contex Manager
class File:
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    # Returns the object that we will perform action (Its the 'as alias').
    def __enter__(self):
        self.file = open(self.file_name, self.mode)

        return self.file

    # Handles the closing even if something unexpeced happen
    def __exit__(self, excp_type, excp_val, traceback):
        self.file.close()


with File("numbers.txt", "r") as file:
    print(file.closed)
print(file.closed)



# We can also create a Contex Manager using a function, via a Decorator

from contextlib import contextmanager

@contextmanager
def open_file(name_of_file: str, file_mode: str):
    """ Everything before yield is like the '__enter()__' method. """
    file = open(name_of_file, file_mode)
    yield file

    file.close()


with open_file("numbers.txt", "r") as file:
    print(file.closed)
print(file.closed)
