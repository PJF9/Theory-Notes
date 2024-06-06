from itertools import compress

"""
    This method is taking as arguments first a normal iterable and
    second an iterable only consist of True, False values

    In the iterator only the True values will be "inserted" 
"""

#? Example
nums = [1,2,3,4,5]
selectors = [True, True, False, False, True]

ex = compress(nums, selectors)

for elem in ex:
    print(elem)