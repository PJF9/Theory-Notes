"""
To describe an `object` we need it's characteristics, namely some data that give us
some information about it. Those data is called `Class Members` or `Attributes`

`Encaptulation` is defined as the ability to `hide` some `attributes` from the outside
world (outside the class). 
Other `Programming Langueages` fully defines encaptualtion using `private` and `public`
class members. Although Python has no sush think.

To declare a `member` (and a `method`) as `private` we add the `prefix` '__', and with
this way this `attribute` (or `method`) is not visible-ish outside the class.
Of course, because there is no such think as `encaptulation` in Python there is a way to
get access `outside` the class using:
    objectName._className__classMember
(the reason is that Python renames those members into '_className__classMember')

Other than `Class Members`, which are varaibles that `apply` only to one object of the
Class, Python provide us a way for a varaible to `apply` to all the objects. Those
varaibles called `Class Variables`

We declare those varaibles at the beginning of the class, just before `__init__()` and
we have `access` to them by reffering to the `name` of the Class: className.variable
We should notice that we can change `Class Variables` for a certain object without 
changing it's value from the other objects: objectName.varaible
"""


class Employee:
    """ Creating the Class Variables """
    nums_of_employees = 0
    raise_amount = 1.03

    def __init__(self, name, salary):
        """ Instanciate the Instance Variables """
        self.name = name
        self.salary = salary
        self.email = self.name + "@gmail.com"
        self.__important_position = False

        Employee.nums_of_employees += 1  # Adding the number of class instances

    def __del__(self):
        Employee.nums_of_employees -= 1

    def apply_raise(self):
        self.salary = int(self.raise_amount * self.salary)
        return self.salary

    def set_important_position(self, aImportant_position=False):
        self.__important_position = aImportant_position

    def get_important_position(self):
        return self.__important_position

    def __super_secreat_message(self):
        return "Super Secreat Message!"

    def call_super_message(self):
        self.__super_secreat_message()


""" Example """
emp_1 = Employee("Petros", 100_000)
emp_2 = Employee("Jacob", 90_000)
emp_3 = Employee("Tony", 110_000)

emp_1.raise_amount = 1.06
print(f"Employee 1: Raise Ammount: {emp_1.raise_amount}")
print(f"Employee 2: Raise Ammount: {emp_2.raise_amount}")
print(f"Employee 3: Raise Ammount: {emp_3.raise_amount}", '\n')

print(f"Number of Employee: {Employee.nums_of_employees}")

emp_2.set_important_position(True)
print(f"Employee 3 Importany Position: {emp_2.get_important_position()}")
print(f"Employee 3 Importany Position: {emp_2._Employee__important_position}")
