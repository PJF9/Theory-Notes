from itertools import count

"""
    With this method we can count numbers ( it is like the range function )
    with the exception that iy counts to infinite

    Arguments:
    1. The starting number we want to start
    2. The step
"""

#? Example
nums = [1,2,3,4]

"""
    Zip function is combining as many iterables we want together
    Zip is finished when the sortest iterable has no more elements
    Zip is actually create a list of tuples
    In the tuple are both the element for the first iterable and the second one
"""
numbers = list(zip(count(), nums))

print(numbers)
