"""
*                            Basic About Tuples                              *
*                            Tuples Indexing                                 *
*                            Tuples Slicing                                  *
*                            Updating Tuple                                  *
*                            Tuples Comprehension                            *
*                            Tuple Unpacking                                 *
*                            N Dimensional Tuples                            *
*                            Copying a Tuple                                 *
*                            Extend Tuples                                   *
*                            Tuples Methods                                  *
*                            Tuples Functions                                *
"""


"""
*                                    Basic About Tuples                                   *

The Tuple data type in Python is an `ordered` collection, just like Lists with the difference,
that the are `immutable` with `mutable` elements, namely we cannot add or delete elements but we
can modify the `mutable` elements that have been stored in the Tuple. As soon us we define the Tuple
we have no method to alter its content.

Tuples are also iterables so we can use them in `for loop` and `if statements` just like Lists.

We can create a tuple with 2 `different` ways. The first is by using '()' and the second with the
function 'tuple()'. For example: 't = (n1, n2, ..., nN)' and 't = tuple(iterable)'

We should notice that if we want to create a tuple with only `one element` we use either: 
't = tuple([n])' or 't = (n,)'
If we skip the comma ',' then t is going to be just an `intager`, or `string` or any other data 
type.

For empty tuple we use: 't = ()' or 't = tuple()'

So in general, Tuples are `exactly` like Lists with the `difference` that they are immutable.
"""


"""
*                                    Tuple Indexing                                   *

Because Tuples as basically `immutable` Lists, every think according to `indexing` that applies on
Lists `applied`, also applies for Tuples.
"""


"""
*                                     Tuple Slicing                                    *

Because Tuples as basically `immutable` Lists, every think according to `slicing` that applies on
Lists `applied`, also applies for Tuples.
"""


"""
*                                      Updating Tuple                                      *

Because Python is a `dynamically typed` there is a way to `modidy` a tuple.

The process is simple. First we `convert` the Tuple into a `List`. Then perform any `modification`
we want to the List and after that `convert` that List into tuple.

And because everything is stored using refferences there is nothing hodling us from use:
't = tuple(modified_list)', where `modified_list` is the `modification` we did on the Tuple list l
'l = list(t)', where t the initial Tuple.
"""


"""
*                                    Tuple Comprehension                                  *

The same that applies on Lists regarding `Comprehension` also applies for Tuples with the difference
that instead of '[]' we use the function 'tuple()', so we can use:
't = tuple(list_comprehensio)', or 't = tuple(comprehension)'

Where a comprehension we mean: 'expr1 if condition else espr2 for elem in iterable'
"""


"""
    *                                 Tuple Unpacking                                        *

The exact concepts also `applies` for Tuples
"""


"""
*                                    N Dimensional Tuples                                     *

The same concept that `apllies` in Lists applies in Tuple.
"""


"""
*                                       Copying a Tuple                                        *

The same concept that `apllies` in Lists applies in Tuple.
"""


"""
*                                       Extend Tuples                                          *

Although Tuples are immutable we can extend a taple using the oprators '+' and '+='

So for example if `t1 = (1, 2, 3)' and 't2 = (10, 20, 30)' then by using 't2 += t1' t2 is
going to have the value (10, 20, 30, 1, 2, 3)

We can also expand the same tuple using '*' and '*='

We should note that those modification doesn't violate the `immutable` behavior. Let's say
for example we are using 't2 += t1' then what is happening is 't1 + t2' are generating a
new tuple. Then we assign this new tuple to t2.
So the original t2 is deleted and t2 now has a new value.
"""


"""
*                                       Tuples Methods                                         *

Python has created for us 2 methods to make our lives eazier working with Tuple.
Those are: 
    count(value): Returns appearences of 'value' inside the Tuple.

    index(element, start): Returns the `first index` position of 'element', starting 
        from index 'start' (default is 0). If 'element' doesn't exists we get `ValueError`.
"""

"""
*                                      Tuples Functions                                        *

All the `functions` that we can use in Lists and `doesn't modify` the List, we can use them
with Tuples.
"""
