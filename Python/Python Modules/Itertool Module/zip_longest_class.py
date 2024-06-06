from itertools import zip_longest

"""
    This method is like the zip function with the exception that it ends
    when the longest iterable has no elements left

    At the elements that has not any pairs are taking the None pair
    We can zip as many iterables we want
"""

#? Example
nums = [1,2,3,4]
letters = ["a", "b", "c", "d", "e"]

comb = zip_longest(nums, letters)

for elem in comb:
    print(elem)