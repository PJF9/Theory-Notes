import logging

logging.basicConfig(filename="employee.log", level=logging.INFO, format="%(levelname)s:%(message)s")

class Company:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        logging.info(f"Employee: {self.fullname} - {self.email}.")

    @property
    def email(self):
        return f"{self.first_name}_{self.last_name}@gmail.com"


    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


emp_1 = Company("Petros", "Floratos")
emp_2 = Company("Jacob", "Floratos")
emp_3 = Company("John", "Smith")