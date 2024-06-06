import logging 
import more_advanced_logging_in_classes


""" 
To solve the previously problem we need to set defferent loggers from each files

"""

# Setting a logger
# The parameter is the name of the logger
# With this method the name of the logger is going to be the name of the module file
logger = logging.getLogger(__name__)

# Set the logger level
logger.setLevel(logging.DEBUG)

# Create a formater for the logging data
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

# Decalre the name of the file we want to logging in
file_handler = logging.FileHandler("test.log")

""" What if we only want the errors appear into the file_handler """
file_handler.setLevel(logging.ERROR)

# Add the formatter to the file
file_handler.setFormatter(formatter)

""" What if we want the debug logging outputed in console """
# Create a stream handler
stream_handler = logging.StreamHandler()
# Formatter
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def div(x, y):
    try:
        resault = x / y
    except ZeroDivisionError:
        # If we also want the traceback 
        logger.exception("Division by zero error")
        
        #logger.error("Division by zero error")
    else:
        return resault

x = 10
y = 0
resault = div(x, y)

logger.debug(f"Div: {x} / {y} = {resault}")