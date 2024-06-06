from collections import OrderedDict
from collections import Counter

"""
    The OrderDict class is a dictionary when keys maintain the order they are inserted
    If we later change the value of a key the key will not change it's position, like
    dictionaries

    This class has all the methods of the dictionary class
"""

#? Creating an OrderDict object
od = OrderedDict()
ob = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)
print(ob)

#? Example
List = ["a", "b", "b", "a", "c", "c", "a", "a", "c"]
counter = Counter(List)
order_dict = OrderedDict(counter)

for key, value in order_dict.items():
    print(f"{key}: {value}")