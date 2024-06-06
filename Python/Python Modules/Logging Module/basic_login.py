import logging
import basic_login_1_2

""" 
    Logging module help us debug our code. Instead of printing the resaults off our programm at console
    with this module we can save them to a .log file 

    Lavels of Logging ( When we set a logging , we’re telling the library you want to handle all events from that level on up. )
    
    __Debug:     Detailed information, only when diagnosing a problem
    __Info:      Confirm that everythig work as expected
    __Warning:   An indication that something unexpected happend
    __Error:     Due to an error the software has not be able to perform some functions 
    __Critical:  A serious error causing the program unable to continue running

    If we set the logging level to info it will include all the above except Debug
    By default the logging level is Warning

"""

# Changing the logging level
# Set a .log, file
# Change the format of the .log file
logging.basicConfig(level=logging.DEBUG, filename="test.log",
            format="%(asctime)s:%(levelname)s:%(message)s") # To logging the program we have to change the output from print to logging.( level )

""" 
The problem with this method is when we try to import another project and logging it too
The resault is that we only get the log file from the module we imported
To resolve this problem see next .py files

"""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y    
    else:
        raise ZeroDivisionError


x, y = 8, 2

add_res = add(x, y)
logging.debug(f"Add: {x} + {y} = {add_res}")

sub_res = sub(x, y)
logging.debug(f"Sub: {x} - {y} = {sub_res}")

mult_res = mult(x, y)
logging.debug(f"Mult: {x} * {y} = {mult_res}")

div_res = div(x, y)
logging.debug(f"Div: {x} / {y} = {mult_res}")
