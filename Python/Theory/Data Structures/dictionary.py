"""
*                       Basics About Dictionaries                                 *
*                       Accessing Elements (Without Methods)                      *
*                       Chnage and Adding Values (Without Methods)                *
*                       Removing Elements (Without Methods)                       *
*                       Looping Dictionary Elements                               *
*                       Dictionary Comprehension                                  *
*                       Merging Dictionaries (Without Methods)                    *
*                       Copying a Dictionary                                      *
*                       Converting Iterable to Dictionary                         *
*                       Dictionaries Methods                                      *
*                       Dictionaries Functions                                    *
"""


"""
*                              Basics About Dictionaries                                  *

In Python Dictionaries data types that contains elements in `key-value` pairs.

Dictionaries are `ordered mutables`, meaning that we can add and delete the key-values
that stores as data and at the same time their elements are also stored the same as the 
insertion order.
We should notice that `keys` are `immutable`, thus we cannot store as key, Sets or Lists,
but values are `mutable` so we can store any data we want.
Dispite Dictionaries are ordered we `cannot store` the same key twice, we will get error.

We can `create` dictionaries using '{}' like sets. Each element contains, as we said, a
key and a value, which are seperated using ':'.
An example is: 'd = {"name": "Petros", 2: [1,2]}'

To create an `empty` Dictionary we use eiter 'd = {}' or the 'dict()' function: 'd = dict()'
"""


"""
*                         Accessing Elements (Without Methods)                           *

Dictionaries are order, that means we can access eazily their elements. To get the values
of a certain key we are using 'v = d[key]'

If the key doen't exists inside the Dictionary it will raise an error.
"""


"""
*                      Chnage and Adding Values (Without Methods)                         *

If a given `key` exists in the Dictionary we can modify its value by simple using:
'd[key] = new_val', where 'new_val' can be any type we want.

If the `key` does not exists in the Dictionary then it will add it, as value the
'new_val' that we are assigned that key.
"""


"""
*                        Removing Elements (Without Methods)                                 *

We can remove a `key-value` pair by using the 'del' keyword: 'del d[key]'

This operation demonstrate the `correlation` of the value with the key.
"""


"""
*                              Looping Dictionary Elements                                 *

Dictionaries are `iterable` objects so we can iterate over then using a simple `for-in`
loop: 'for key in d'. With the same mind we also can use `if key in d`

We should notice by this loop, the Dictionary `returns` us only its `keys`, to access also
the values, we either user the method 'items()' or simply be using 'd[key]' we have also
the value that is correspoding to that key.

To make our lives a bit more eazier Python has created the methods 'keys()' and 'values()'
that we can use in a `for loop` to iterate over the `keys` or the `values` accordingly.
"""


"""
*                                 Dictionary Comprehension                                     *

The same way List, Sets and Tuples `Comprehension` works, also works with Dictionaries with the
difference the an expression is being consists by 2 parts, a `key` and a `value`

For example: 'd = {i:i**2 if (i % 2 == 0) else i** + 1 for i in range(10)}'

Other that ':' we can store the `key-value` pair into a Tuple.
"""


"""
*                            Merging Dictionaries (Without Methods)                            *

Python has given us a lot of ways to `merge` 2 or more dictionaries. Other than `for-loop` 
we can use:  'd = {**d1, **d2, ..., **dn}'

We can also use the operators '|', '|=':  'd = d1 | d2 | ... | dn'
"""


"""
*                                    Copying a Dictionary                                          *

The `same` that applies on Lists applies also on Dictionaries. Both `shallow` and `deep` copy
"""


"""
*                             Converting Iterable to Dictionary                                *

We have 2 ways of `converting` an iterable (except from Strings) into a dictionary. Either by
using the function 'dict(..., namei = vali, ...)' or the function 'dict()' with 'zip()'

The `first` way let's say we have List: 'l = [n1, n2, ..., nN]', to convert it to a Dicitonary
by simply: 'd = dict(name1 = l[0], name2 = l[1], ..., nameN = l[N-1])', where as
`name` we refer as the name of the key that the value 'ni' will refer.
(Note that accepts only names like `name`, `abcd` not `"name"`, or `123`)

The `second` way let's say we have the same List 'l' and we want to convert it to a Dictionary.
We can use 'd = dict(zip(l, l))'

We should notice that we can `convert` any type into a Dictionary, as long as the Dictionary is
created with those 2 methods

Finally, of course we can create custom `function` an with a `for-loop` to fill the Dictionary
with values.
"""


"""
*                                  Dictionaries Methods                                      *

Python has created some `methods` to help us when working with Dictionaries. Those are:
    clear(), copy(), fromkeys(), get(), items(), keys(), pop(),
    popitem(), setdefault(), update(), values()

clear(): Removes all the keys and the values of the Dictionary.

copy(): Returns a shollow copy of the Dictionary.

fromkeys(iterable, val): Converting 'iterable' into aDictionary. The `elements` of 
    'iterable' are going to be the keys of the Dictionary and as values each key will
    initialize with 'val' (default is None). It returns the Dictionary not modifying
    and the `caller`.

get(key, val): Returns the value that correspond to 'key'. If 'key' doesn't exist it
    will return the 'val (default in None).

items(): Returns a view object that contains all the `key-value` pairs of the Dictionary
    as Tuples in a List. If we change the Dictioanry the view object will change.

keys(): Returns a view object the contains all the keys of the Dictionary as a List. 
    If we change the Dictioanry the view object will change.

pop(key, val): Delete and returns the value that has the specified key.If 'key' doesn't
    exists ait will return the 'val' (default is None).

popitem(): Deletes and returns the last `key-value` pair that has inserted into the Dictionary.

setdefault(key, val): Returns the value of 'key'. If 'key' doesn't exists it will add the
    'key':'val' to the dictionary and return the 'val' (default is None).

update(dict): Adds 'dict' to the Dictioanry.

values(): Returns a view object the contains all the values of the Dictionary as a List.
    If we change the Dictioanry the view object will change.
"""


"""
*                                   Dictionaries Functions                                   *

The same functions that applies to Lists, also applies to Dictionaries with the difference 
that applies only to the `keys`, not to the values.

For example `sorted()` is sorting the Dictionary according to the keys.
"""
