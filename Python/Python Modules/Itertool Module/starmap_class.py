from itertools import starmap

"""
    It's like the map function with the difference that this method is taking
    as an arument a zip fucntion of iterables
"""

#? Example
s = starmap(lambda x,y: x**y, list(zip([1,2,3,4,5], range(1, 6))))

for elem in s:
    print(elem)