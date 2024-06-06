"""
This module is a very `powerfull` module that contains every `mathematical` function and
constant we want.

1) The `constants` that contains are: 
    pi = 3,14...
    e = 2,71...
    τ = 6.28..
    inf = infinity
    nan = not a number

2) The `trigonometric` functions that we can use are:
    sin(x), cos(x), tan(x)
    asic(x), acon(x), atan(x), atan2(x, y) = arctan(x/y) (a = arc)
    sinh(x), cosh(x), tanh(x)

    (Where x is mesured in rads)
    We can convert degrees into rads using:
        degress(x): Converting rads to degrees
        radians(x): Converting degrees to rads.

3) We can calculate the `distance` and the `norm` of point, that is donoted by Tuples:
    dist(p, q): The Eyclidian Distance of point (Tuples) p, q
    hypot(*cords): The norm of the point that is described by '*cords'

4) `Exponents` and `logarithms`:
    pow(x, y): The difference between the opererator '**' is that 'pow' first convert
        the arguments into `floats`
    exp(x), sqrt(x), isqrt(x): floor of exact square root of x
    log(x): ln(x), log(x, base), log10(x), log2(x)

5) `Rounding` and `Absolute` value:
    floor(x), ceil(x), modf(x): the decimal and integer part, fmod(x, y): the intager part
    of x/y
    fabs(x): |x|, copysign(x, y): sign(y)*|x|

6) `Factorial` and some `Functions`:
    factorial(n): n!, comb(n, k): combination k of n, perm(n, k): permutation (n)k (μεταθεση)
    gcd(n, m), erf(z): error function, gamma(z): Γ(z)

7) `Sumations` and `Product`:
    fsun(iterable): the sum of 'iterable's elements, prod(iterable)

8) `Checks`:
    isinf(x), isnan(x), isfinite(x): True of not inf nan
"""
