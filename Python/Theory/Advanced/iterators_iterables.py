"""
*                                        Iterators                                       *

A class (or an object) is called `iterator` when it can gives us its elements sequentialy
(one by one) with the dunder method '__next__()'
This method is called in `for loops` and makes posible the syntax: 'for x in iter'

Other than '__next__()' an iterator has to also initialize the method '__iter__()'
which is called by default from the `for loop` to give us this capability

We can refer a class as an `iterator` if it contains the above 2 methods.

We should notice that '__iter__()' has to return the reference to the object (self) and 
'__next__()' should other than returning an element, to raise `StopIteration` so the `for
loop` will know when to stop (when we run out of elements).

To convert an object to an `iterator` we use the function 'iter()' that is the overload of 
the '__iter__()' method and to get the next element using 'next()' which is also the
overload for '__next__()' 
"""


"""
*                                        Iterables                                          *

An object is an `iterable` if we can iterate over them, namely it is possible to to take its
elements one by one.

Iterables are:
1) Our own classes that has defined '__iter__()' and '__next__()'
2) Every sequence, like Lists, Tuples, Sets, String, Frosen Sets
3) Non sequencial stractures like Dictionaries

An iterator, we can say that is a `pointer` to one element of the iterable and has the option
to move through the elements.

When we are using iterables with `for loops` then for loops convert the `iterable` into an
`iterator` and then return this object that has the capability of using 'next()', so at the
end of each loop, the 'next()' function is executed until it raises `StopIteration`
"""


"""
*                                    Functions for Iterators                                   *

There are a lot of fucntions that apply on `iterators`

The `first` type of functions are the complex type conversions:
    list(iter), tuple(iter), set(iter), frosenset(iter), dict(enumerate(iter))

Also we have the calculating functions:
    min(iter), max(iter), sum(iter), all(iter), any(iter)

Then we have:
    enumerate(iter, start=0), zip(*iters), reversed(iter), sorted(iter), map(iter), filter(iter)
"""


# Creating a for loop
iterable = iter([1, 2, 3, 4, 5])

while True:
    try:
        value = next(iterable)
    except StopIteration:
        break


# Creating the 'range' function
class Range:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.reversed = True if self.start > self.end else False

    def __iter__(self):
        self.previous_number = self.start
        
        return self

    def __next__(self):
        if self.reversed:
            if self.start <= self.end:
                raise StopIteration
        else:
            if self.start >= self.end:
                raise StopIteration

        return_number = self.previous_number
        self.start += self.step
        self.previous_number = self.start

        return return_number
