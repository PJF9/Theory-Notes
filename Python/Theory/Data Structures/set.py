"""
*                            Basic About Sets                                *
*                            Accessing Set Elements                          *
*                            Set Comprehension                               *
*                              Copying a Set                                  *
*                            Set Methods                                     *
*                            Set Functions                                   *
"""


"""
*                                    Basic About Sets                                        *

In Python Sets just like Lists and Tuples are used for `storing` multiple elemenet in memory.

The key difference of Set is that its an `unorder` data type meaning that their elements
are stored in RAM not in the order we pass them, but via a mathematical function (hash)
So indexing in a Set doesn't make sense.

Another difference is that Sets accepts only distinct values, so we cannot store in a Set
duplicate data. If we try to create a Set with duplicate data then it is simply going to
ignore them and throw them away.

Sets are `mutable` with `immutable` elements, meaning that we can add and remove elements
from them but we cannot modify the elements that have been stored inside of the Set.

To `create` a set we use 's = {n1, n2, ..., nN}' or 's = set(iterable)'

To create an `empty` set we can't use 's = {}' because in that way s is going to be a `Dictionary`.
So we use instead the set function: 's = set()'

Also, `slicing`, `unpacking` and `N-dimensional Sets` does not make sense when working with sets.
"""


"""
*                                  Accessing Set Elements                                    *

As we discused `indexing` in Sets doesn't make sense so for `accessing` their element use for
loops or `converting` them to an ordered data type like Lists.

Because they are also `iterables` we can use `for elem in Set` and `if elem in Set`
"""


"""
*                                  Set Comprehension                                          *

The same concept that applies on List and Tuples, also apllies on Sets.
"""


"""
*                                     Copying a Set                                            *

The same concept that applies on List and Tuples, also apllies on Sets.
"""


"""
*                                     Set Methods                                             *

Python has creted for us a lot of method to work with Sets. Those are:
    add(), clear(), copy(), difference(), difference_update(),
    discard(), intersection(), intersection_update(), isdisjoint(),
    issubset(), issupersubset(), pop(), remove(),
    symmetric_difference(), symmetric_difference_update(),
    union(), update()

add(element): Adds the given element to the Set.

clear(): Removes all element from the Set.

copy(): Returns a shallow copy of the Set.

differecne(*sets): Returns a set that contains only the elements af `caller` Set that
    doesn't exists on 'sets'. Can also be activated with the '-' operator.

difference_update(*sets): Perform the same task like 'difference()' with the difference 
    that it doesn't return a new set rather modifying the caller set. Can be activated
    with the '-=' operator.

discard(element): Removes the 'element' from the Set. If it doesn't exists then this
    method does not raise error, unlike 'remove()'.

intersection(*sets): Returns a new set that contains only the elements that exists
    in all 'sets'. Can also be activated using the operator '&'.

intersection_update(*sets): Perform the same as 'intersection()' with the difference that
    it doesn't return a new set rather changes the caller Set. Can be activated using the
    '&=' operator.

isdisjoint(set): Returns True if the two Sets have not same elements.

issubset(set): Returns True if the caller Set exists inside 'set'.

issupersubset(set): Returns True if the caller Set contains 'set'.

pop(): Removes and returns a random item from the Set.

remove(element): Removes 'element' from the Set. If doesn't an error will be raised.

symmetric_difference(set): Returns a new Set that contains all the distinct elements 
    from the two Sets. Can be activated using the '^' operator.

symmetric_difference_update(set): Performs the same as 'symmetric_difference()' with the
    difference, instead of creating a new Set it changes the caller Set. Can be activated
    with the '^=' operator.

union(*sets): Creating a new Set that contains all the elements from both the caller Set
    and all 'sets'. Can be activated using the '|' operator.

update(set): Adding 'set' to the Set. Can be activated using the '|=' operator.
"""


"""
*                                       Set Functions                                      *

Because Sets are iterables, all the functions that applies to Lists (and does not
changes individual element) applies also for Sets.
"""
