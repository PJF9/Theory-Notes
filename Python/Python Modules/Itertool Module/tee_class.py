from itertools import tee

"""
    This method helps us copy an iterator ( converted iterable ) to others iterables
    
    Arguments:
    1. The iterable
    2. The total copies we want
"""

#? Example
numbers = [0,1,2,3,4,5]

copy1, copy2, copy3, copy4, copy5 = tee(numbers, 5)

for elem in copy1:
    print(elem, end=" ")

print()

for elem in copy5:
    print(elem, end=" ")