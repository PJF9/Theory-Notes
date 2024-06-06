"""
After developing a program and writing all the code it's time for some `testing` to
be done. In software comapnies `testing` is a seperate division. It so valuable
process because it spots all the `unexpected` bugs that the developer misses out. 

There are 2 `categories` of testing:
1) Unit Testing: Checking only one function or class.
2) Integration Testing: Checking how all the functions or classes act together. 
    Usually comes after `unit testing`

To perform `unit testing` to a method or a class we use the module `lib/unittest.py`
Although there are much more to work with.

A way to `unit testing`, without this module, that Python provide us it `assert`
statements. The syntax is:
    assert condition, "Error Message - If the condition fails"
If 'condition' fails then an `AssertError` is being raised and stops execution.


Now we will see how the module `unittest` gives us the ability to test out code.
First there are some rules that we `have` to obey for our own shake:
1) Creating a different file to test, that import all functions or methods for testing.

2) Creating a class that inherits from `unittest.TastCase` that gives us access to all
    assertion methods: 
        assertEqual(a, b)         : checks `a == b`
        assertNotEqual(a, b)      : checks `a != b`
        assertTrue(x)             : checks `x == True`
        assertFalse(x)            : checks `x == False`
        assertIs(a, b)            : checks `a is b`
        assertIsNot(a, b)         : checks `a is not b`
        assertIsNone(x)           : checks `x is None`
        assertIsNotNone(x)        : checks `x is not None` 
        assertIn(a, b)            : checks `a in b` 
        assertNotIn(a, b)         : checks `not a in b` 
        assertIsInstance(a, b)    : checks `isinstance(a, b)`
        assertNotIsInstance(a, b) : checks `not isinstance(a, b)`

3) We define the tests as different methods that starts with 'test_' and then the name of
    the test we want to perform.

4) In the body of the test we calling (not returning) any of those assertion we want

The same logic can be extend for testing a class, with the difference that we add a method
named 'setUp()' that create any helping object (of the class we are testing) we want.
"""

def my_sum(sth):
    s = 0
    for num in sth:
        s += num
    
    return s

assert my_sum((1,2,3)) == 6, "Some bug exists..."


""" example using unittest module """
def my_sum(*nums):
    s = 0
    for num in nums:
        s += num

    return s
     

import unittest

class My_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(my_sum(1,2,3), 6)

    def test_2(self):
        self.assertEqual(my_sum(), 0)

    def test_3(self):
        self.assertEqual(my_sum(9, 1), 0)
