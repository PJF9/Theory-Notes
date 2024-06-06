from itertools import permutations

"""
    This method returns all the combinations of the iterable, with duplicates
    A duplicate is ( a,b ) and ( b,a )

    Arguments:
    1. The iterable
    2. The total size of the returned tuple

    The difference between this method and the combination one is that this one
    gives us ALL the combinations between the iterable but the combination
    method NOT
"""

# Example
numbers = [0, 1, 2]

ex1 = permutations(numbers)
for elem in ex1:
    print(elem, end=" ")

print()

ex2 = permutations(numbers, 2)
for elem in ex2:
    print(elem, end=" ")
