from itertools import filterfalse

"""
    This method work exactly like the compress one with the
    defference that it applies the defferent concept

    Only the Flase values will be "inserted" into the iterable
    Instead a iterable is taking as a first argument a functions
"""

#? Example
nums = [1,2,3,4,5]

def f(n):
    if n < 3:
        return True
    return False

ex = filterfalse(f, nums)

for elem in ex:
    print(elem)