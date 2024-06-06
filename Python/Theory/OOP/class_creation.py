def funct(x):
    class Hallo:
        def print_hello(self):
            return "Hello! " * x

    return Hallo


class Text:
    pass


c = funct(2)
print(c.print_hello(c))

""" The only reason we can create something like that is that classes in fact
are objects!!! """
""" Class difines the rules/methdos/atributes... for an object, the metaclass
 difines the rules for a class ( difines how the class id created )"""

# Print the class that these objects belong
# print(type(funct))
# print(type(Text()))
# print(type(Text))

# We can also create a class like that
# First is the name, Then the inherirance ( we need , at the end ) and Then the
# atributes and the methods


class L:
    def show(self):
        return "Hallo!"

# Add methods to our class


def add_atr(self):
    self.major = "Comp. Science"


Test = type("Test", (L,), {"name": "Petros", "add_attribute": add_atr})
t = Test()
# Set value
t.age = 18
t.add_attribute()

print(t.name)
print(t.age)
print(t.show())
print(t.major)
