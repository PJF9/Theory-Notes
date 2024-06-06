from itertools import accumulate
import operator

"""
    This method is doing operations with the element of the iterable
    This method can combine with the operator module to get the different operands

    Argument:
    1. The iterable
    2. The operand ( Default is + )

    Usefull for both the average and also the factorial of a numbers
"""

#? Example
numbers = [1,2,3,4,5]

ex1 = accumulate(numbers)
for elem in ex1:
    print(elem, end=" ")

print()

ex2 = accumulate(numbers, operator.mul)
for elem in ex2:
    print(elem, end=" ")