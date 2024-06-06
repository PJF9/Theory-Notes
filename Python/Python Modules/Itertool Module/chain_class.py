from itertools import chain

"""
    This class is creating an iterator to help us iterate over iterables 

    Lets say we would to iterate over 300 lists with 1000 element each list
    To iterate over all of them we have to convert them into a single one
    This approach can cause memory overflow

    So to prevent this for happening we use the chain itertool

    Arguments:
    - The only argument the iterables
"""

#? Example
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4, 5]
names = ["Petros", "Jacob", "Tony", "Nick"]

# The wrong way
comb_list = letters + numbers + names
print(comb_list)

# Via itertools
comb_list = chain(letters, numbers, names)

"""
    Now comb_list is a iterator
    So to print all the list elements we need a for loop
"""

for elem in comb_list:
    print(elem, end=" ")