"""
Abstract Classes are `classes` that we cannot create objects. There are very usefull
in classes that making an object does not make sense, like the class `Animal` that is
the base of a lot derived classes, or the class `Person` and also when we want to
define some methods that `derived` classes has to initialize.

Those method are called `Abstract Methods` and are methods that we have not defined
their bodies.

To convert a method into an abstract method we need the decorator '@abstractmethod'
form 'lib/abc.py' and also out class to inherite 'ABC' for the same module.
"""

from abc import ABC, abstractmethod


class Example(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def method(self):
        pass
