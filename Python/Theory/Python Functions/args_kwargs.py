"""
The rule for working both with `value` arguments and `keyword` arguments:
    First we are passing every `value` argument we want and then the `keyword` arguments.

Python privide us with a way for passing as many `arguments` we want, using the `special`
argument `*args` for `normal` arguments and `**kwargs` for `keyword` arguments.

Python stores the parameters inside `*args` as a Tuple and inside `**kwargs` as a
Dictionary.

As before, first we need to pass the `*args` and then the `*kwargs`

We should notice that the names `args` and `kwargs` are not required, we could have
any name we care for passing them the parameters, but by convesion these 2 names are
the standards.
"""


def test(*args, **kwargs):
    print(args)
    print(kwargs)


test(9, [3,3], "Hello", (10, 11, 12), dict(), name="Petros", age=20)
