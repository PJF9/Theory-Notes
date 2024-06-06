"""
Inheritance is a concept of `Object Oriented Programming`, which a class contains all
the `Instance Variables`, `Class Variable` and `Methods` of another class. The first
class is called `Derived` and the other `Base`.
We say that `Derived` class `inherits` the `Base`
We should notice that `Derived` class extends Base, because other that `Base`'s methods
and attributes the `Derived` class can declare any other method and attribute we like.

The syntax we use for inheritance:
    class Base:
        ...

    class Derived(Base):
        ...

The process to find and create the `attributes` that an object has first implies 'has-a'
To find `inheritance` we use the relation: 'is-a'
For example a horse is-a mammal and a mammal is-a animal

If a method of the `Base` achive different fucntionality on the `Derived` object we have
the option to `override` it, meaning to redefine it.

When `initializing` the `Derived` class we need somehow to also `initialize` the attributes
of the `Base` class. Python does that using the function 'super()'
This function returns an objects that `represents` the `Base` class so by simply using
'super().__init__(*attributes)' we can initialize all the attributes of the `Base` class.
By convesion the attributes of `Base`, are passed first before the attributes of `Derived`
and we call 'super()' at the top of 'self.__init__()'

(With the same logic, if we want to access a method of `Base` we use: 'super().method(...)'
(The same functionality can be achive with 'BaseClassName.__init__(self, *attributes)' and
'super(DerivedClassName, self).__init__(self, *attributes)')

In other `Programming Languages` encaptulation defines other than `public` and `private`
also `protected` members. Those are attributes or methods that are `visible` in all
`Derived` classes but `not visible` outside of the classes. In Python we hav no way
of defining `protected`.
Although the convesion is to denote every `protected` member of method as: 'self._attribute'
and 'def _method(self, ...)'
(using the prefix '_')

There is nothing that stops us for defining `Multiple Inheritance`, meaning that a class can
inherit more than 1 `Base` class. We use the same syntax and we pass the `Base` classes
seperated by comma.
Using `Multiple Inheritance` the function 'super()' repreasents the `Base` class that we
pass first, so to `initialize` the attributes of all `Base` classes we use 'Base.__init__(self, ...)'
Although is a very `usefull` concept we need to use it with `cautious`, to not cause any problem, like
the `diamond  problem`
Those problem can be used either with `interfaces` of `abstraction`

"""


class Company:
    raise_amount = 1.02

    def __init__(self, fname: str, lname: str, salary: int):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def email(self) -> str:
        return f"{self.fname}_{self.lname}@company.com"

    def salary_raise(self):
        self.salary = int(self.salary * Company.raise_amount)


class Developer(Company):
    raise_amount = 1.04

    def __init__(self, fname: str, lname: str, salary: int, prog_lang: str,
                 experience: int):
        super().__init__(fname, lname, salary)

        self.prog_lang = prog_lang
        self.experience = experience

    def salary_raise(self):
        self.salary = int((self.salary * (Company.raise_amount +
                                          Developer.raise_amount - 1)))


class Manager(Company):
    raise_amount = 1.05

    def __init__(self, fname: str, lname: str, salary: int,
                 employees: list = []):
        super().__init__(fname, lname, salary)

        self.employees = employees

    def salary_raise(self):
        self.salary = int((self.salary * (Company.raise_amount +
                                          Manager.raise_amount - 1)))

    def add_empl(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def rem_empl(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)


class Employee(Company):
    def __init__(self, fname: str, lname: str, salary: int, age: int):
        super().__init__(fname, lname, salary)

        self.age = age

    def salary_raise(self):
        self.salary = int(self.salary * Company.raise_amount)


class CEO(Developer, Manager):
    def __init__(self, fname: str, lname: str, salary: int, prog_lang: str,
                 experience: int, is_good: bool, employees: list = []):
        Developer.__init__(self, fname, lname, salary, experience, prog_lang)
        Manager.__init__(self, fname, lname, salary, employees)

        self.is_good = is_good
