"""
Pyhton has 3 rules dealing with arguments and modifications:
1) `Immutbale` arguments `don't` keep their changes after function call.
2) `Mutable` arguments generaly keep their changes if the modification comes from
    a `method`.
3) `Mutable` arguments don't keep any change if we `assign` them to different objects.
"""


def test1(x):
    x = 9
    
    return x

x = 10
print(f"Prev: {x}", end=", ")
test1(x)
print(f"after: {x}")


def test2(x):
    x.append(3)
    x = [1, 2, 3]

    return x

x = [3, 6, 9]
print(f"Prev: {x}", end=", ")
test2(x)
print(f"after: {x}")


def test3(x):
    x[0] = [10]
    x = [1, 2, 3]
    x[0] = [11]

    return x

x = [[3, 6, 9], [3, 6, 9]]
print(f"Prev: {x}", end=", ")
test3(x)
print(f"after: {x}")
