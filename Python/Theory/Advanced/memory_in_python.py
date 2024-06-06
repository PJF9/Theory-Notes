"""
Python has a `special` way of storing data and values. It has 2 memory spaces: 
the `identifier` space and the `object` space.

As `identifier` we define every `variable` that we are using in our program and 
as `object` every `value` that identifier are assign to through our program.
So in the example 'x = 9', 'x' refers as identifier and the intager 9 as `object`

The `assignment` operator works like a bind between an identifier and an object and
tells us that this identifier is `linked` with that object

We can see the `memory` location of each object using: 'id(obj)'. We should notice
that Python `forbits` us to see the memory location of each identifier. By using
the function 'id()' to an identifier we are seeing the `location` of the object
that this identifier is bind to.

We should, also notice that each object is stored only once in `object space` so by
`assigning` the same object to `different` identifiers, Python doesn't create many
objects rather binds `all` those identifiers with the same object.

Next, by `assigning` 2 identifiers `together` (x2 = x1), then the identifier x2 will
be bound with the same object as x1.

In other `Programming Languages` this concept is called `reference`


Now we are going to see how Python stores more complex data types, `objects` in the
memory. Let's say we have the List 'l = [3, 9]', then as we said 'l' is the identifier
and '[3, 9]' is the object. But '3' and '9' are also objects so it binds 'l[0]' with '3'
and l[1] with '9'.

We should notice that 'l' and '[3, 9]' are different. 'l' is described by l[0] and 
l[1], '[3, 9]' is a temporary List object, not the bind of `l` into the `object` space.

So If we write 'l2 = [l[0], l[1]]', `l` and 'l2' are different identifiers and are 
bound to different objects, their elements are bound to the same object.

Let's say that 'l1 = l', then 'l1' is bound to the same object as 'l', so their elements
are also bound to the same objects, thus by changing one List the other will also change.
To prevent that we use 'l1 = l.copy()' or 'l2 = l[:]'

What if we had 'l = [[1,2], [3,4]]' and tried: 'l2 = l.copy()'. Then 'l2' and 'l' are
bound to different objects, but their elements, that are also Lists (mutables) are bounded
to the same object. See, before the elements were imutable so we didn't care so much because
either way we cannot change their value (let's say at 132543 location in object space always
the  will be stored value 8).

But Lists are, as I said mutables, so we can change their values. So by changing l[0]
also l1[0] will be changed. Thats why we name the previous copying method as `shallow copy`.

To prevent that we use another method that we call `deep copy` (we can find it on 'lib/copy.py')
"""

x = 9
print(f"x: {id(x)}, 9: {id(9)}")
y = 3
print(f"y: {id(y)}, 3: {id(3)}")
y = x
print(f"x: {id(x)}, y: {id(y)}, 9: {id(9)}, 3: {id(3)}")
x = "Hello"
print(f"x: {id(x)}, y: {id(y)}, 9: {id(9)}, 3: {id(3)}, Hallo: {id('Hello')}", end='\n\n')


l = [3, 9]
l1 = [l[0], l[1]]
l2 = [3, 9]
print(f"l: {id(l)}, [3, 9]: {id([3, 9])}, l[0]: {id(l[0])}, l[1]: {id(l[1])}, 3: {id(3)}, 9: {id(9)}", end=", ")
print(f"l1: {id(l1)}, [l[0], l[1]]: {id([l[0], l[1]])}, l1[0]: {id(l1[0])}, l1[1]: {id(l1[1])}", end=", ")
print(f"l2: {id(l2)}, [3, 9]: {id([3, 9])}, l2[0]: {id(l2[0])}, l2[1]: {id(l2[1])}", end='\n\n')

l = [3, 9]
l1 = l
print(f"l: {id(l)}, l1: {id(l1)}, l[0]: {id(l[0])}, l[1]: {id(l[1])}, l1[0]: {id(l1[0])}, l1[1]: {id(l1[1])}")


from copy import deepcopy

l = [3, 9]
l1 = deepcopy(l)
print(f"l: {id(l)}, l1: {id(l1)}, l[0]: {id(l[0])}, l[1]: {id(l[1])}, l1[0]: {id(l1[0])}, l1[1]: {id(l1[1])}")
