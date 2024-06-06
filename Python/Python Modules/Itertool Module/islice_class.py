from itertools import islice

"""
    This itertool help us grab a sub-iterable from the original iterable
    
    Arguments:
    1. The iterable we want to take the sub-iterable
    2. The starting index position ( default is 0 )
    3. The ending index position ( not including the end )
    4. The step

    If we skip the second argument the new second is going to be the prior third
"""

#? Example
numbers = [0,1,2,3,4,5,6,7,8,9]

ex1 = islice(numbers, 4)
for elem in ex1:
    print(elem, end=" ")

print()

ex2 = islice(numbers, 2, 4)
for elem in ex2:
    print(elem, end=" ")

print()

ex3 = islice(numbers, 3, 8, 2)
for elem in ex3:
    print(elem, end=" ")