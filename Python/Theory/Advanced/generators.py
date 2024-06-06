""" 
A Generator is a function that creates an iterator more eazily, with less
code. In fact is a function that doesn't get destroyed after all its code
is run, but sustain each state (the values of local variables) when the 
fucntion is called again.

To create a Generator we use the same syntax like a normal function, but
when it's time to return a value, instead of using the keyword 'return' we
use the 'yield'.

After creating the Generator we create an iterator base on this function
and then with the '__next__()' method we can get all the iterator elements.

In Python we can also use Generator Expressions. They are an even simpler
way of writting Iterators. The syntax is the same like list comprehension
with the difference instead of '[]' we are using '()'.

Python has aslo created for us some methods that apllies on Generators.
This methods only apply for the Generator object outside the Generator
function. Methods:
    send(value) -> This method is sending a value to the Generator. To
        use this method we need to get the yield value on a variable.
        By sending a value to the Generator we affect the next element
        of it. After the send the Generator is going to give us the
        elements after the send value.

    close() -> This method closes, ends the iteration without the Generator
    reaches it's end.

    throw() -> Throws an exception to the Generator.

    To use all the Generator methods we need to crea the Generator object.
    Else we can't use them.
"""


""" Creating a range() function using Generator """
def Range(start: int, end: int, step: int = 1):
    is_reversed = True if start > end else False
    number = start

    while True:
        if is_reversed:
            if number <= end:
                break
        else:
            if number >= end:
                break

        yield number
        number += step


""" Creating a sentencae Generator """
def Sentence(string: str):
    for word in string.split():
        yield word


""" Generator Expressions """
gen_1 = (num for num in range(10))
gen_2 = (num for num in range(10) if num % 2 != 0)
gen_3 = (num if num % 2 != 0 else num ** 2 for num in range(10))


""" Generator's Methods """
from random import randrange

def send_gen():
    value = 0
    for _ in range(10):
        ret = yield value
        
        if ret is None:
            value += 1
        else:
            value += ret + 1


def close_exeption_gen():
    num = 1
    while True:
        yield num

        num += 2
