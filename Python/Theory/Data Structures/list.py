"""
*                            About Lists                                       *
*                            List Indexing                                     *
*                            List Slicing                                      *
*                            Modifying List (Without Methods)                  *
*                            List Comprehension                                *
*                            Unpacking List Elements                           *
*                            N Dimensional Lists                               *
*                            Copying a List                                    *
*                            Extend Lists (Without Methods)                    *
*                            List Methods                                      *
*                            List Functions                                    *
*                            List Dunder Methods                               *
"""


"""
*                                     About Lists                                      *

The List data type in Python is an impementation of a `dynamic array`. Thus it is
storing elements in sequencial order inside RAM. The key difference between
Python Lists and let's say C++ vectors is that in Lists we can store more than one
data type.

Lists are one `class` of the 4 Python's builds that used to store elements. The other 3
are Tuple, Set and Dictionary.

We should notice that Lists are `mutable` with `mutable` elements, namely we can add or
delete elements from the List and also change the `mutable` elements that have been stored.
An example of non mutable (called immutable) class is Strings (we can't do s[n] = 'P').
Lists are also `iterable` data types, meaning that we can iterate and loop over their
elmenets using for loops as: 'for elem in l' and if statements: 'if elem in l'

Also unlike Sets and Dictionaries, Lists `keep` their elements positions after
initialization as we have created them (keep their elements order).

We can create Lists using brackets: 'l = [...]'
"""


"""
*                                 List Indexing                                           *

We can select/modify/extract a given element from a List (let's say at the i-th position)
using l[i-1] (it's i-1 becuase numbering starts at 0). We call 'i-1' as 'index'. So the
element at the 0-index position is the first element of the List

Along side positive (and zero) indexes we also have `negative`. The -1-index simply means
the last element of the List. So by passing -i as an index we are getting the i-th element
starting from the `end` of the List.
"""


"""
*                                 List Slicing                                             *

Despite of single elements Python provide us a way to select `more than one` element from
our Lists. The method is called 'Slicing'.

The syntax is as follows: l[start:end:step]

Where `start` is the index of the first element we want to select, `end` is the index after
the last element we want to select (meaning that l[end] will not be inlcude in our `sublist`)
and at last `step` by how many indexes we want to select elements starting from `start`
(default is step=1, and also cannot be 0)

Note that there are not at all limitations. We can have positive, negative, zeros and also
`ranges` that don't even make sense, like [0:0:1]

Some `variations` of slicing are, l[:end], l[start:], l[:] or l[::-1]

The `first` variation selects all the elements starting at 0-index throuht index end-1
The `second` variation select all the elements starting from start-index through and 
including the last element.
The `third` variation selects every element from the list and it's use is powerfull
(we discuss it on 'Copying a List')
The `last` variation reverses the List.
"""


"""
*                         Modifying List (Without Methods)                         *

As we know Lists are `mutable` data types so we can change and `modifying` them
as we want.

We can modify a List either using `methods` or by `indexing`, `slicing` or even
with the keyword `del` for deleting an element or a range.

For example l[i] = n, l[start:end] = [...] and del l[i], del l[start:end:step]

We should notice that inside [...] when using slicing to modify a List, there are
no limitations of how many elemenets [...] will replace [start:end], we can have
more, less, it doens't matter.
The only limitation is when using `step`. If [start:end:step] contains 'n' elements
then inside [...] we should have 'n' elements.

Other than 'l[start:end] = [..]' we can also use 'l[start:end] = v1, v2, ..., vm
(where as vi we can pass any data type we want)
"""


"""
*                            List Comprehension                                      *

Let's say we want an easy and fast way to create a List using some other iterable
data type. The solution is 'List Comprehension' 

The syntax is: l = [expression for element in iterable if condition]

Which means that as elements of l, we will choose all the expression that involves
the elements of iterable that passes a condition. The condition is also called the
`filter` of the comprehension.

We can use a more `advanced` and `powerfull` syntax:
l = [expression1 if condition1 else (expression2 if condition2 else ...) for element in iterable]

The key take away from this syntax is:
l = [expression1 if condition else expression2 for element in iterable]
"""


"""
*                                Unpacking List Elements                                   *

Instead of using slicing and indexing for selecting certain elements we can use 'unpacking'

It works as follows, let's say we have a List l with 'n' elements. Then if xi are variables
we can assign to each xi an element of the List:
x1, x2, ..., xn = l

Which means that x1 = l[0], x2 = l[1], ..., xn = l[n-1]

We can also use 2 `wildcards`. The first is '_' which means that if we place this wildcard
at index i, the i-th element of the List will `not be selected`, it will be skipped.
The other wildcard is '*', which means that I want this variable to `collect all the remaining`
elements, thus variables with that wildcart are being placed at the end of the sequence.

The example: x1, _, *x2, _ = l, will assign x1 = l[0] and x2 = [2:n-2]
"""


"""
*                                   N Dimensional Lists                                       * 

All we talked about so far we applied to 1-d Lists. There is nothing holding us from expanding
this knowledge in `N-d Lists`

We can create 2-d Lists as follows: l2d = [[...], [...], ..., [...]]
We should notice that there is no limitation of how many elements each [...] could have

And also 3-d Lists: l3d = [[[...], ..., [...]], [[...], ..., [...]], ..., [[...], ..., [...]]]

When working with highter dimensional Lists we need to adapt indexing, slicing and comprehension
to the `correct` number of dimensions.
"""


"""
*                                      Copying a List                                         *

If we want to copy l1 into l2 we can't use the assignment operator (l2 = l1)
Because Python is a `dynamic Language` everything is being stored as a reference of some values
inside RAM. 

So if 'x = 3', then x is a refference that has the value 3. If we do 'y = x' then y will be a
refference of x that has the value 3. So by `modifying` y, x will be `affected` as well. Both
x and y has the same space in `memory` (we can see using id(x), id(y))

To correctly copy l1 to l2 we can use either the method 'copy()', the function 'list()' and also
slicing for `shallow copy`.
If we want `deep copy` then we need to use the function 'deepcopy()' from 'lib/copy.py'

So let's talk about `shallow` and `deep` copy.

Shallow copy only `create` a copy (new object) from the original object but storing as `refferences`
the `elements` of that objects.
By using the example of 1-d List we can't see any difference between shollow and deep copy
But when we are working with 2-d Lists let's say: 'l2 = l1.copy()' and we try to do
l2[0][0] = n, both l2 and l1 element on the (0,0)-index will be changed to n
(The same expands in N-d Lists)

From the other hand, `deep` copy prevents that from happening becuase it create a `copy` 
form the original object and then recursivly create copies for also the `children` of the
original List and then the `children` of the `childrens` of the original object and so on.
By using `deep copy` we are deleting every link between the 2 objects.

So to summury we can `shallow` copy 2 lists using:
l2 = l1[:], l2 = list(l1)

And for deep copy
from copy import deepcopy
l2 = deepcopy(l1)
"""


"""
*                          Extend Lists (Without Methods)                             *

Let's say we have 2 Lists, l1 and l2 and we want to `concatinate` them. The way we 
can do that without methods are using '+', '+=' operators.

We should also notice that using '*', '*=' with some intager n (as right object) we can 
repeat our List n amount of times.
"""


"""
*                                    List Methods                                          *

Python has created some usefull methods to help us modifying and getting information from
a List. Those are:
    append(), insert(), extend(), clear(), pop(), remove(), 
    reverse(), sort(), copy(), count(), index()

append(element): Inserting 'element' at the `end` of the List (n-th index)

insert(position, element): Inserts 'element' into 'position'-index position. All elements
    next or equal to this index will move one place to the right.

extend(iterable): Inserting at the `end` of the list the elemenets of 'iterable'

clear(): `Removes all` the elements of the List. Equivelant with 'l.clear()' we can
    use 'del l' and 'del l[:]'

pop(positon): Deletes the element that lives in 'posiiton'-index position (default is -1).

remove(element): Deletes the first element that has the value 'element' from the list.

reverse(): Reversing the list.

sort(reversed, key): Implementing `TimeSort` to sort the list. If 'reversed' is False
    (by default) it will sort the list in ascending order, otherwise descending. 'key' refers
    to the creteria of the sorting (etc the length if we want to sort a string-list)

copy(): Returns a `shallow copy` of the original list.

count(value): Rerurn the `appearances` of 'value' inside the list.

index(element, start): Returns the `first index` position of 'element', starting 
    from index 'start' (default is 0). If 'element' doesn't exists we get `ValueError`.
"""

"""
*                                     List Functions                                      *

Python along side methods has created some function to make our lives eazier. The
`difference` between `methods` and `functions` is that methods `modify` the List and doesn't
`return` a new List. On the other hand function don't `modify` the List rather `returns` a
new list with all modifications. Those functions are:
    len(), list(), max(), min(), sum(), sorted(),
    reversed(), enumerate(), zip(), map(), filter(),
    all(), any()

len(iterable): Returns the length of the 'iterable'

list(element): Creates a List out of the given element.

max(iterable): Returns the maximum value of 'iterable'

min(iterable): Returns the minimum value of 'iterable'

sum(iterable): Returns the sum of the elements of 'iterable'

sorted(iterable): Returns a new sorted list from 'iterable'

reversed(iterable): Retrurn an iterator to the reversed list from 'iterable'

enumerate(iterable, start): Returns an iterator that contains the maching of the indexes, 
    starting from start (default 0), with each individual element of 'iterable' in tuples.

zip(*itearbles): Returns an iterator that contains an matches the i-th element of each
    iterable to a tuple. The length of the iterator will be the minimum length among all
    iterables.

map(function, iterable): Returns an iterator to a map object that contains the iterable
    that has created from 'iterable' after apllying 'function' to each element

filter(function, iterable): Returns an iterator to a filter object that contains the 'iterable's
    elements that have passed the 'function' (should return True/False)

all(iterable): Returns True if all the 'iterables's elements are no False. As false can
    be counted 0 or empty objects.

any(iterable): Returns False if all the 'iterables's elements are False.
"""


"""
*                                   List Dunder Methods                                             *

The last think we will talk about List are 'double underscore methods', also called dunder methods.
Are special methods, that have created inside the class but we can not access them with the '.'.
We can access them via eiter an operator, or a function. Those are:
    __del__(),  __repr__(),  __str__(),  __bytes__()m __format__(),
    __lt__(), __le__(), __eq__(), __ne__(), __gt__() __ge__(),
    __add__(), __sub__(),  __mul__(),  __matmul__(), __truediv__(),
    __floordiv__(), __abs__(), __max__(), __min__(), __sum__(),
    __int__(), __float__(), __list__(), __complex__(),
    __round__(), __trunc__(), __ceil__(), __floor__(), __len__(),
    __getitem__(), __setitem__(), __delitem__(), __iter__(),__next__()


__del__(self): for del() function. It is called when a List object is being deleting.

__repr__(self): for repr() function. It returns a string. Intended for developers to debug.

__str__(self): for str() function. Return a string. Intended for users to see a useful output.
    If not implemented, __repr__() will be used as a fallback.

__bytes__(self): for bytes() function. Return the byte string representation of the object.

__format__(self): for format() function. Evaluate formatted string literals like '%' for percentage
    format and 'b' for binary.

__lt__(self, anotherObj): for < operator.
__le__(self, anotherObj): for <= operator.
__eq__(self, anotherObj): for == operator.
__ne__(self, anotherObj): for != operator.
__gt__(self, anotherObj): for > operator.
__ge__(self, anotherObj): for >= operator.

__add__(self, anotherObj): for + operator.
__sub__(self, anotherObj): for - operation on object.
__mul__(self, anotherObj): for * operation on object.
__matmul__(self, anotherObj): for @ operator (numpy matrix multiplication). (doesn't work
    for lists)

__truediv__(self, anotherObj): for simple / division operation on object.
__floordiv__(self, anotherObj): for // floor division operation on object.
__abs__(self): make support for abs() function. Return absolute value.

__int__(self): support for int() function. Returns the integer value of the object.
__float__(self): for float() function support. Returns float equivalent of the object.
__complex__(self): for complex() function support. Return complex value representation 
    of the object.

__trunc__(self): for trunc() function of math module. Returns the real value of the object.
__round__(self, nDigits): for round() function. Round off float type to 2 digits and return it.
__ceil__(self): for ceil() function of math module. The ceil function Return ceiling value
    of the object.
__floor__(self): for floor() function of math module. Return floor value of the object.


__len__(self): for len() function. Returns the total number in any container.
__getitem__(self, key): to support indexing. Like container[index] calls 
    container.__getitem(key)explicitly.
__setitem__(self, key, value): makes item mutable (items can be changed by index), like 
    container[index] = otherElement.
__delitem__(self, key): for del() function. Delete the value at the index key.

__iter__(self): returns an iterator when required that iterates all values in the container.
__next__(self): returns the next element if exist of the iterator List. If it doesn't it raises
    StopIteration error.
"""
