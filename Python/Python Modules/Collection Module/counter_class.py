from collections import Counter

"""
    Counter is a sub-class of dictionary
    This class is taking as an argument an iterable and returns a dictionary
    In this dictionary the key is an element and the value is the total appearecne of the iterable

    Because the Counter class inherite from the dictionary one, we can use all the dictionary methods too

    The additional methods are:
    1. Element
    2. Most_common
    3. Subtract

    ? Element Method
    This method returns an iterator object, so to see the values we need to concatinate it to an iterable
    ( Returns only the original items, not the dyplicates )

    ? Most_common Mehtod
    This method returns a list of tuples ( at the first tuple position is the item and at the second one the total times )

    ? Subtract Mehtod
    Takes as an argument an list or a dictionary and removes the element from the original object with the argumented one

"""

#? Creating the Counter Object
c1 = Counter()
c2 = Counter(".....12221113")
c3 = Counter([1,2,3,1,2,3,1])
c4 = Counter({1:3, 2:4, 3:1})
c5 = Counter(A=2, B=3)

#? Printing the Counter objetcs
print(c1)
print(c2)
print(c3)
print(c4)
print(c5, "\n")

#? Update method
c1.update([1,1,1,2])
print(c1, "\n")

#? As a dictionary we can access each item key using:
print(c1[1])
print(c2["."])
print(c3[3])
print(c4[2], "\n")

#? Element method
print(list(c2))

#? Most_common method
print(c3.most_common())

#? Subtract method
cm = [".", ".", ".", ".", ".", 1, 1, 1, 1, 1, 1, 3, 3, 3]
cM = [".", ".", 1, 1, 1, 1, 3, 3]
c = Counter(cm)
c.subtract(cM)
print(c)