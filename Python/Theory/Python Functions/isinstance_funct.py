"""
Retrurns True, if a given object has a certain data type, otherwise False

Syntax:
    isinstance(obejct, (type1, type2, ..., typeN))

If object's type exists in the Tuple, it will return True
"""

print(isinstance(2, int))
print(isinstance(2, str))
print(isinstance([1,2,3], (list, int)))
