"""
A `good` class is a concept of the real world. To `achive` that we need to contain
to our class every `has-a`, meaning everything that this concept includes.

Those `has-a` are the `Class Members` and nothing stops us for declaring more
complex type, like objects from our `Classes`
"""

class Storey:
    def __init__(self):
        self.people = 0


class Building:
    def __init__(self, number_of_storeys):
        self.storeys = [Storey() for _ in range(number_of_storeys)]

    def add_people(self, storey, peoples):
        if (storey > len(self.storeys)):
            print(f"Building has no {storey} storeys, has only {len(self.storeys)}.")
        elif (storey <= 0):
            print("You can add only on positive storeys.")
        else:
            self.storeys[storey - 1].people += peoples

    def show(self):
        for i in range(len(self.storeys)):
            print(f"Storey {i}: {self.storeys[i].people} peoples.")


b = Building(3)
b.show()
print()
b.add_people(1, 4)
b.add_people(2, 5)
b.add_people(3, 1)
b.show()
print()
b.add_people(0, 1)
b.add_people(-1, 10)
b.add_people(4, 2)
