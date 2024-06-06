from itertools import combinations

"""
    This class is returning all the combinations, without duplicates
    A duplicate is ( a,b ) and ( b,a )

    Arguments:
    1. The iterable
    2. The size of the combination tuples ( the returned tuples )

    This method is NOT giving us all the combinations between the iterable
    It doesn't reorder the iterable
"""

# Example
numbers = [1, 2, 3, 4]

ex1 = combinations(numbers, 2)
for elem in ex1:
    print(elem, end=" ")

print()

ex2 = combinations(numbers, 3)
for elem in ex2:
    print(elem, end=" ")
