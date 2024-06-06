import logging


# Setting a logger
# The parameter is the name of the logger
# With this method the name of the logger is going to be the name of the module file
logger = logging.getLogger(__name__)

# Set the logger level
logger.setLevel(logging.INFO)

# Create a formater for the logging data
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

# Decalre the name of the file we want to logging in
file_handler = logging.FileHandler("student.log")
# Add the formatter to the file
file_handler.setFormatter(formatter)

# Add the file to the logger
logger.addHandler(file_handler)



class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        logger.info(f"Student: {self.fullname} - {self.email}")

    
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}.{self.age}@gmail.com"


s1 = Student("Petros", "Floraots", 17)
s2 = Student("Jacob", "Floratos", 18)
s3 = Student("Test", "User", 20)