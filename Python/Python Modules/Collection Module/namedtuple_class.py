from collections import namedtuple

"""
    This class returns a tuple with the names for each position in the tuple
"""

#? Create a namedtuple object
Student = namedtuple("Student", "fname, lname, age")
s1 = Student("Petros", "Floratos", 17)
print(s1)
print(s1.lname)

#? We can create a namedtuple object by a list
List = ["Jacob", "Floratos", 19]
s2 = Student._make(List)
print(s2)

#? Create an instance of the namedtuple class by an already created one
s3 = s2._asdict()
print(s3)

#? Change field values
s1 = s1._replace(age="18")
print(s2)
