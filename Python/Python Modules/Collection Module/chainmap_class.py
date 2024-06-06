from collections import ChainMap

"""
    The ChainMap is used to combine several dictionaries
    It returns a list of dictionaries

    It has all the method of a dictionary
"""

#? Create a ChainMap object
dict1 = {"a": 2, "b": 3}
dict2 = {"a": 3, "c": 1, "d": 4}

cm = ChainMap(dict1, dict2)
print(cm)

#? We can access values by it's key ( if we have duplicate keys then it will get the value of the first key )
print(cm["b"])
print(cm["a"])

#? If we update one dictionary them the chain map is changing as well
dict2["e"] = 6
print(cm)

#? Add new element to the ChainMap object ( it will be added to the start of the ChainMap )
dict3 = {"f": 2, "g": 1}
cm = cm.new_child(dict3)
print(cm)
