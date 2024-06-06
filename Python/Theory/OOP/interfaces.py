"""
In some `Programming Languages` does not allow a class to inherite more than one
Base classes.
Those languages, like Java and C#, are using a concept named `intefaces`

Interfaces are `packets` of methods that a class can inherite. There is no limitaiton
to how many of those packes a class can inherite

In Python we can achive `interfaces` using abstract methods.
"""

# An example that demonstrates interfaces is the following:

from abc import ABC, abstractmethod
from math import pi


class Geometric_Objects_Interface(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Geometric_Objects_Interface):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Resizable(ABC):
    def resize(self):
        pass


class Circle_Resizable(Circle, Resizable):
    def __init__(self, radius):
        Circle.__init__(self, radius)

    def resize(self, param):
        self.radius += param


c = Circle_Resizable(1)
print(c.area(), c.perimeter())
c.resize(2)
print(c.area(), c.perimeter())
