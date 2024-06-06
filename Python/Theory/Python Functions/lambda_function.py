"""
Lambda Functions are small anonymous functions, that can take as many 
arguments we want, but we must evaluate them only in on expression.
We should notice that Lambda Functions have a small period of lifetime. 

Syntax:
    funct_name = lambda argumenst: expression

The power of using lambda functions show up if we want a small function
inside a normal function (like filter() or map()).
"""

""" The same task can be performed using lambda function """
def funct(x):
    return x+1
print(funct(8))

funct2 = lambda x: x+1
print(funct2(8))


""" Another way of using lambda functions """
def funct3(x):
    return lambda a : a*x
myfunct = funct3(2)
print(myfunct(6))


""" Using them with map() and filter() """
List = [0,1,2,3,4,5,6,7,8,9]
print(list(map(lambda x : x+1, List)))
print(list(map(lambda x : x+1, filter(lambda n : n % 2 != 0, List))))