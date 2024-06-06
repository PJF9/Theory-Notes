from itertools import cycle

"""
    This method cycles the values of an iterable over and over again
    to the infinity
"""

#? Example
c = cycle([1,2,3])
for _ in range(10):
    print(next(c))