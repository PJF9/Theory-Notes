"""
Contains functions to generate number numbers and to pick random elements from
an iterable.

First we need to understand how a computer is generating random numbers. It starts
from a number, named `seed` and performs a complex mathematical function to generate
another number. Then applying the same function to that number to generate another
`random` number and so on.

We set a `seed` using: 'seed(x)' where x is number we want to start generating.
By default 'x = None' which means that as a seed will set as the current time of the
system.

Other than 'seed(x)', which for the same input x will generate the same sequence we have
the option to save a `state` of the random number generator and use it to continue from the
same number later on.
Using 'getstate()' returns a state-object that we can pass it in 'setstate()' to continue
from this specific value.

1) To generate intager values we use:
    randrange(stop): in the range [0, stop]
    randrange(start, stop [, step]): in the range [start, stop] with step
    randint(a, b): in the range [a, b]

    The random integers of those functions follows `Uniform Distribution`

2) To generate real values we use:
    random()         : uniform distribution in (0, 1)
    uniform(a, b)    : uniform distribution in (a, b)
    triangular(a, b) : triangular distribution in (a, b)
    betavariate(a, b): beta destribution in (a, b)
    gammavariet(a, b): gamma distribution in (a, b)
    expovariete(l)   : exponental distribution with parameter l
    gauss(m, s)      : gaussian with m, s
    normvariete(m, s): a faster gaussian distribution

3) To choose random elements from iterables we use:
    choice(iter)
    shuffle(iter)
    choices(iter, k=n): Creates a List length n that contains random elements of iter.
        (It can contain duplicate elements)
    sample(iter, k)   : Creates a List length k without duplications
"""

from random import choices

a = [1, 2, 3]
print(choices(a, k=4))
