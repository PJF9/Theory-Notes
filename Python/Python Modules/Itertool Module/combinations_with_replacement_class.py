from itertools import combinations_with_replacement

"""
    This method is like the combinations one, but it's also gives us iterable
    element with the same symbol ( we can get the (a, a) )

    This is the difference between this one and combination

    Arguments:
    1. The iterable
    2. The size of the returned tuple
"""

# Example
numbers = [0, 1, 2, 3]

ex1 = combinations_with_replacement(numbers, 1)
for elem in ex1:
    print(elem, end=" ")

print()

ex2 = combinations_with_replacement(numbers, 2)
for elem in ex2:
    print(elem, end=" ")
