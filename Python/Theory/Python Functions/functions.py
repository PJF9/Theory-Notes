"""
A function is a block of code that is created to perform a specific task.
Syntax: 
    def funct_name(parameters):
        ...
        return return_value

Note that code after the return keyword will not executed. In order to
terminate the function we can use the return keyword with not any value.

After you've created a function, in case we want the block of code that is
containing to run, we should 'call' the function.
Syntax:
    funct_name(arguments)

We are writting functions so our code can remain D.R.Y ( do not repeat 
yourself ). We are also writting functions because this way we can break
our code in  smaller parts ( eazier debugging and writting )

About the parameters, we can pass as many we want, whatever data type we
want. A function can return one on more values, that we can store them in
variable(s).
Syntax:
    var1, var2, ... = funct_name(parameters) 



We have 3 Rules that we have to follow to better understand the arguments
    Rule 1: 
        Immutable arguments (argumnents that their values is constand)) 
        don't maintaining the changes that occur at the function

    Rule 2:
        Muttable arguments are maintainig the changes that occur at the 
        function (this change must be originate from methods).

    Rule 3:
        Mutable arguments don't maintaining the changes that occur at the
        function if the change isn't originated from methods.



The arguments we were working with called Positional arguments. But we also
have Keyword Arguments. Keyword arguments are arguments that we pass using 
the name of the function parameter.
Syntax:
    def hello(name, age, condition):
        ...

    hello(age=20, name="Petros", good)

Keyword Arguments must be written first of the Positional ones.



In python we can predeclare some arguments (Default Arguments)
If the user don't pass a value for those arguments, in the program they 
will have the default value.
Syntax:
    def hello(name, age, condition="Good"):
        ...

The Default Arguments must be after all the normal ones



We can also have a function that takes as many argumnets we want.
Syntax:
    def add(*args):
        ...

We can also pass key-value pair arguments (Keyword Arguments) with the same
logic.
Syntax:
    def hello(**kwargs):
        ...


Last but not least Python has the option for Factoty Function. These
functions is constructing other functions.
Syntax:
    def factory_funct(power):
        def nth_power(number):
            return number ** power

        return nth_power
"""

# Rule number 1 Example:
def f1(arg):
    print(arg)
    arg = "Changed"
    print(arg)

s = "Initial"
f1(s)
print(s, "\n")


# Rule number 1 Exaple:
def f2(arg):
    print(arg)
    arg.append(3)
    print(arg)

l = [1,2]
f2(l)
print(l, "\n")


# Rule number 1 Exaple:
def f3(arg):
    print(arg)
    arg = [3]
    print(arg)

l = [1,2]
f3(l)
print(l, "\n")


# Many args
def add(*args):
    print(args)
    s = 0
    for num in args:
        s += num

    return s

print(add(1,2,3,4,5), "\n")


# Many keyword args
def hello(**kwargs):
    print(kwargs)
    return kwargs


hello(name="Petros", age=18)
print()


# Factory function
def factory_funct(power):
    def nth_power(number):
        return number ** power

    return nth_power


square = factory_funct(2)
print(square(9), "\n")


# Another Example
def digits_number(number):
    string_num = str(number)
    int_nums = []

    for i, num in enumerate(string_num, start=1):
        print(f"Digit number {i}: {num}")
        int_nums.append(int(num))

    return int_nums

digits_list = digits_number(10177)
print(f"\nDigits list: {digits_list}")
