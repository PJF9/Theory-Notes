"""
Zip Function return a zip object (which is an iterator) of the coupling of each
iterable passed as arguments, meaing that as a first elements it will contain the
first element of the first iterable, the first elemenet of the second iterable,
and so on. As second element the second element from the first iterable, the second
element from second itrable and so on.

Syntax:
    zip(*iterable)

We should note that the length of the zip object will be the minimum length of all
itarables.
"""

x = ["Peter", "Jacob", "Floratos"]
y = [1, 2, 3, 4]
z = [[1,2], [2,3]]

for zip_element in zip(x, y, z):
    print(zip_element)
