"""
To describe an object we need its `actions`, its funcionality, namely some fucntions
that perform, modify or even extract informations about the object. Those functions
are called `Class Methods`.
All the `objects` of our class have the same methods. We way that a method `acts`
on an object when the object `calls` the method: objectName.method(...)

We can `classify` those methods into 4 categories
1) Regular Methods
2) Class Methods
3) Static Methods
4) Special Methods

Regular Methods: The 'normal' methods that the user defines. We pass `self` as the 
    first argument.

Class Methods: The methods that have the '@classicmethod' decorator. Those methods does
    not depend on the objects, instead are depending to the class and they are a chracteristic
    of the class. Usually contains extra `information` about the class, the `Class Varaibles`
    and are also usefull for modifying them. We pass `clc` as the first argument.

Static Methods: The methods that have the '@staticmethod' decorator. Those methods does
    not affect nor `interact` with both the class and the objects. They are some functions
    that are stored inside the class and gives us `more functionality`, meaning that usually
    taking as argument objects of the class and returning some result. With `Static Methods`
    we are giving more readability to the code. We don't pass some special `keyword` as
    first argument.

Special Methods: Also called `Dunder` and `Megic`, are methods that have already created for us,
    and we are initialize them and `fit` them to our goals and our functionality. With those
    methods we can achive `operator overloading` and making the interaction of our objects
    musch more clean and eazy.

About `Special Methods` we should notice that, let's say we have overloaded the operator '+' and
that A, B are 2 objects of out class. Then by using `A + B` we reffer to 'A.__add__(B)'
So 'A' is the `caller` object and 'B' is the parameter.
Also by defining '<', '<=', '==' by default Python creates '>', '>=' and '!=', so we don't need
to place them in our code.
Also notice that in case of passing different type objects, via the 'isinstance()' function we
can treat each type accordingly.

The Dunder Methods are (and many more):
1) Rational Operators (must return Boolean):
    __lt__, __le__, __eq__, __ne__, __gt__, __ge__ 

2) Binary Operators (must return an object of the class):
    __add__, __sub__, __mul__, __matmul__, __truediv__, __floordiv__, __div__, __mod__,
    __pow__, __max__, __min__, __sum__, __lshift__, __rshift__, __and__, __or__, __xor__
    (using the prefix 'r' we define those for right-side operations)
    (using the prefix 'i' we define '+=', '-=', etc: returns `self`)

3) Unary Operators (must return an object of the class):
    __neg__, __pos__, __invert__, __abs__, __round__, __ceil__, __floor__, __int__,
    __float__, __str__, __repr__, __bytes__, __complex__, __list__ 
    (neg: for '-a')
    (round() takes as optional `ndigits`)
    (floor() and ceil() is on 'lib/math.py')
    (repr() represents the object in form 'object(*params)')

4) __len__, __getitem__, __setitem__:
    (with len() and __getitem__(): '[]', we can loop over our item, Python knows how to create
    a basic iterator)

5) __call__:
    (converts our object into a function)

6) __new__ __init__, __del__:
    (__new__(): creates an empty object that is created from the general class 'object'. Every object
    in Python inherits from 'object' (etc dunder methods). So instead of leaving to us the process of
    creating an object Python, automaticly calls the command super(className, cls).__new__(cls))
    (__init__(): initializes the created object. It gives it the attributes we need)
    (__del__(): is called when our object has no more references to it. It is called from the
    `garbage collector` and deallocate the memory space.)

7) __iter__, __next__:
"""


class Employee:
    number_of_emplopyees = 0
    alternative_number_of_employees = []
    raise_ammount = 1.03

    def __init__(self, first_name: str, last_name: str, salary: int):
        """ Initializes the `Class Members` with the user passed values """
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

        Employee.number_of_emplopyees += 1
        Employee.alternative_number_of_employees.append(
            f"{self.first_name}-{self.last_name}-{self.salary}")

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        """
        Converts the object into a string. The difference with __str__()
        is that __repr__ is used for programmer to programmer and in most cased
        it contains some information about the object.
        """
        return f"Object: first_name = {self.first_name}\n        last_name =" \
            f" {self.last_name}\n        salary = {self.salary}$"

    def __add__(self, other_pay) -> int:
        return self.salary + other_pay

    def __radd__(self, other_pay) -> int:
        return self.salary + other_pay

    def __iadd__(self, other_pay) -> int:
        return self.salary + other_pay

    def __del__(self):
        Employee.number_of_emplopyees -= 1
        Employee.alternative_number_of_employees.pop()

    def __eq__(self, right) -> bool:
        if (self.fullname == right.fullname):
            return True
        return False

    def __lt__(self, right) -> bool:
        if (self.salary < right.salary):
            return True
        return False

    def __le__(self, right) -> bool:
        if (self.salary <= right.salary):
            return True
        return False

    def email(self) -> str:
        return f"{self.first_name}_{self.last_name}@gmail.com"

    def to_string(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.salary}"

    @property
    def fullname(self) -> str:
        """
        This decorator is 'converting' a method into an `Attribute`
        (we can call it with no '()'). Because we can't use '()' we need
        to create some more methods to initialize it. This jobs is for the
        '@propertyMethod.setter' decorator.
        """
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, name: str):
        self.first_name, self.last_name = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None

    @classmethod
    def get_number_of_employees(cls) -> int:
        return cls.number_of_emplopyees

    @classmethod
    def get_alternative_number_of_employees(cls) -> int:
        return len(cls.alternative_number_of_employees)

    @classmethod
    def set_raise_amount(cls, raise_ammount: float):
        cls.raise_ammount = raise_ammount

    @staticmethod
    def object_from_string(strirng: str):
        first_name, last_name, salary = strirng.split('-')
        return Employee(first_name, last_name, salary)
