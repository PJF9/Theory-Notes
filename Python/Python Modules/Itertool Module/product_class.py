from itertools import product

"""
    This method gives us all the combinations, with duplicates and words with
    same iterable element It's like permutation except it also gives us let's
    say elements with same letters

    Arguments:
    1. The iterable
    2. The number of times that a letter can exist is a returned tuple
    The second argument is also the size of the returned tuple

    We can name the product method also permutations with replacement
"""

# Example
numbers = [0, 1, 2, 3]

ex1 = product(numbers, repeat=2)
for elem in ex1:
    print(elem, end=" ")

print()

ex2 = product(numbers, repeat=1)
for elem in ex2:
    print(elem, end="")
