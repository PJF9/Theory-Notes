from collections import defaultdict

"""
    The defaultdict class woorks exactly like the dictionary class with the exception
    that does not throw KeyError if we try to access a non-existed key

    Intead it initialize the key with the element of the data type we have passed 
    at the declaration. The data type is called default_factory

    Default Factory:
    - int: 0
    - float: 0.0
    - str: ''
    - bool: False

    The defaultdict class has all the method that the dictionary class has
"""

#? Creating defaltdict objects
dd1 = defaultdict(int)
print(dd1)
dd1["one"] = 1
dd1["two"] = 2
print(dd1["three"])
print(dd1)

#? Example
count = defaultdict(int)
for name in "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split():
    count[name] += 1
print(count)