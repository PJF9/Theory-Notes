"""
Map Function return a map object (which is an iterator) of the results after applying
the given function to each item of the given iterable.

Syntax:
    map(function, iterable)

We should notice that we can pass more that one iterables it.

The same functionality can be performed using list comprehension
"""

List = [0,1,2,3,4,5,6,7,8,9]

def funt(x):
    return x ** 2

new_list = []
for element in List:
    new_list.append(funt(element))
print(new_list)


new_list = list(funt(element) for element in List)
print(new_list)


new_list = list(map(funt, List))
print(new_list)


list1 = [10, 20, 30, 40]
list2 = [9, 11, 13, 15]

new_list = list(map(lambda x, y: x + y, list1, list2))
print(new_list)