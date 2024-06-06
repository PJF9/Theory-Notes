"""
*                            Basic About Frosen Sets                         *
*                            Accessing FrosenSet Elements                    *
*                            Frosen Set Comprehension                        *
*                            Copying a Frosen Set                            *
*                            Frosen Set Methods                              *
*                            Frosen Set Functions                            *
"""


""" 
*                               Basic About Frosen Sets                             *

Frosen Sets are just like sets with the difference that they are `immutable`, thus
we cannot add or remove elements after `initialization`.

Because Frosen Sets are `immutables` with `immutable` elements so can be stored as 
`keys` in Dictionaries or elements in Set.

We should notice that just like Set, we cannot have `duplicate` elements in a Frosen Set.
If we try, this data type will `ignore` them

We can create a Frosen Set using: 'f = frosenset(iterable)' or 'f = frosenset()'
"""


"""
*                            Accessing Frosen Set Elements                            *

The same regarding `accessing` Set's elements applies on Frosen Set's.
"""

"""
*                             Frosen Set Comprehension                               *

The `same` rules of Comprehension that applies to all the other types also applies on
Frosen Sets with the difference that we need to `convert` the comprehension to a 
Frosen Set ojbect using the function 'frosenset()'
"""


"""
*                              Copying a Frosen Set                                 *

The same concept that applies on the other types also applies on Frosen Sets.
"""


"""
*                              Frosen Set Methods                                     *

Every method of Sets that does not affect the `caller` Set also is a method for
Frosen Set. Those are:
    copy(), difference(), intersection(), isdisjoint(),
    issubset(), issupersubset(), symmetric_difference(), 
    union()

copy(): Returns a shallow copy of the Frosen Set.

differecne(*fr_sets): Returns a set that contains only the elements af `caller`
    Frosen Set that doesn't exists on 'fr_sets'. Can also be activated with the '-'
    operator.

intersection(*fr_sets): Returns a new set that contains only the elements that exists
    in all 'fr_sets'. Can also be activated using the operator '&'.

isdisjoint(fr_set): Returns True if the two Frosen Sets have not same elements.

issubset(fr_set): Returns True if the caller Frosen Set exists inside 'set'.

issupersubset(fr_set): Returns True if the caller Frosen Set contains 'set'.

symmetric_difference(fr_set): Returns a new Frosen Set that contains all the distinct
    elements  from the two Sets. Can be activated using the '^' operator.

union(*fr_set): Creating a new Frosen Set that contains all the elements from both the
    caller Set and all 'fr_set'. Can be activated using the '|' operator.
"""


"""
*                                Frosen Set Functions                                  *

All the functions that applies on Sets also applies on Frosen Sets.
"""
