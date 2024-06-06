"""
Filter Function returns an `iterator` to the items filtered by a function whcich
only the elements that passes are `accepted` to be inlcuded to it

Syntax:
    filter(function, iterable)
    
The same functionality can be performed using `comprehension`.
"""

List = [0,1,2,3,4,5,6,7,8,9]

def is_odd(x):
    return x % 2 != 0

print(list(filter(is_odd, List)))
print(list(filter(lambda x: x % 2 != 0, List)))
