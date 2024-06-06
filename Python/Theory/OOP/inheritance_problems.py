"""
Let's say we want to call a `parent` method that exists on both derived's base classes.
? Which method is going to be executed ?

Another problem is let's say that both base classes `inherite` the same class.
? Will derived class inherite twice the `grandparent` class ?

Python has overcome those problems using a simple model: 
Linearizes all the classes (both derived and base), simply putting them into an `array`
using an algorithm named `C3 Linearization` so an `order` is defined between the base
classes of derived.
This order is called `MRO`, standing for Method Resolution Order and we can access this
order using the method 'mro()' or the class

So for the `first` problem the method that is going to be called is the base class that comes
first in `MRO`

And for the `second` problem, simply if a class exists inside the array it does not adding
it again, so we have `no duplication` of data.

A think to notice is that each class inherites from the class `object` which provides all the
dunder methods (using abstract methods)
"""


# An example that makes thinks clear is the following:
class A:
    def __init__(self):
        print("Entering A")
        super().__init__()
        print("Exiting A")


class B1(A):
    def __init__(self):
        print("Entering B1")
        super().__init__()
        print("Exiting B1")


class B2(A):
    def __init__(self):
        print("Entering B2")
        super().__init__()
        print("Exiting B2")


class D(B1, B2):
    def __init__(self):
        print("Entering D")
        super().__init__()
        print("Exiting D")


D()
print(D.mro())
