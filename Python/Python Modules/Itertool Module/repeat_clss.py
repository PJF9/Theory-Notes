from itertools import repeat

"""
    This method is taking as an argument any object and repeats is all over again

    Arguments:
    1. The element we want to repeat
    2. The total ammount of times ( default is infinite )
"""

#? Example
r = repeat((1,0,1))
for _ in range(10):
    print(next(r), end=" ")

print()

square = list(map(lambda x, y: x**y, repeat(2), range(10)))
print(square)

