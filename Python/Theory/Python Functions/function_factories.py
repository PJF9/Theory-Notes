"""
Function Factories are `functions` that creating other functions, meaning that they are
returning an `inner` function.

We can do that because in fact, `fucntions` are objects that belongs to the calls `function`.
So we have no `limitation` of creating a function inside a function.

In other Programming Languages we `cannot` do such thing, because in those `functions` are
procedures no objects
"""

def factory_power(power):
    def nth_power(number):
        return number ** power
    
    return nth_power

cube = factory_power(3)
print(f"2^3 = {cube(2)}")


def polynomial_factory(*args):
    if (len(args) == 3):
        def quadradic_eq(evaluate):
            res = 0
            i = 1
            for coeff in args:
                res += (coeff * (evaluate ** (len(args) - i)))
                i += 1

            return res

    return quadradic_eq

pol = polynomial_factory(3, 2, 2)
print(pol(1))

