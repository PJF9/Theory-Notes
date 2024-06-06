from collections import deque

"""
    The deque class is a list optimized ( has one job, that does it better than anyone )
    for inserting and removing elements

    We can add an element at both ends of the deqeu
    To add to the right we use the append method
    To add to the staer we use the appendleft method

    We can also apply the same logic with removing elements
    Remove the last element: pop
    Remove the first element: pop_left

    We can also clear the deque with the clear method
    As an output we will see None

    The deque has the most of list's methods
"""

#? Creating deque objects
List = [1,1,2,2,3,3]
d = deque(List)
print(List)

#? Add elements
d.append(4)
d.appendleft(0)
print(d)

#? Remove elements
d.pop()
d.popleft()
print(d)

#? Count method
print(d.count(1))
