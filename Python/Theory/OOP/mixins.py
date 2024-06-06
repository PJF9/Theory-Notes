"""
Mixins comes from `Programming Languages` that don't allows multiple inheritance and
are very `similar` to interfaces, meaning that they are classes used to `provide` methods
to another class and the difference is that mixins `implement` those methods instead of leaving
them blanc, like interfaces do.
"""

# An example that demonstrate mixins is the following:

class ComperableMixin:
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        return (self <= other) and (self != other)
    
    def __gt__(self, other):
        return not (self <= other)
    
    def __ge__(self, other):
        return (self == other) or (self > other)
    

class Intager(ComperableMixin):
    def __init__(self, n):
        self.n = n

    def __eq__(self, x):
        return (self.n == x)
    
    def __le__(self, x):
        return (self.n <= x)
    

""" With just 2 methods we have created all the comperable operators"""

print(Intager(3) != Intager(4))
print(Intager(3) > Intager(9))
