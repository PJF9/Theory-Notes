"""
    Decorators are functions that improve the functionality of a class or a
    function without affecting them. Decorators are implemented via factory
    functions.

    To create a Decorator we need to create a function that takes as an
    argument another function (factory function). At the body of that function
    we should define one more wrapper function, which will be the updated
    function (both our old function and the new functionality).

    At the calling procedure we call the Decorator:
        decorated_funct = decorator(our_funct)
        decorared_funct()

    Or we can use the '@' before our function name following with the name of  
    the decorator function and at the calling we only use the original's
    function name.

    We are not limited about the number of Decorators a function can have. We
    can have as many Decorators we want.

    In the special case that our function takes some arguments we pass those
    arguments at the wrapper function. If we know the exact number of the 
    arguments we should pass them one by one, but if we have no idea we should
    use the *args, **kwargs arguments. The *args is a tuple with all positional
    arguments and the **kwargs is a dictionary with all the keyword arguments.

    Also we can have a Decorator that takes some arguments. Then we need to
    make our Decorator a wrapper function, meaning that we need to create a
    new function and inside of it will be the Decorator. This new function will
    take the parameters we want for the Decorator.

    Instead of function Decorators we can have also class Decorators.
"""

""" Basic Example using Decorators """
def decorated_with_lines(funct):
    def wrapper():
        print('=' * 20)
        funct()
        print('=' * 20)

    return wrapper

def decorated_with_stars(funct):
    def wrapper():
        print('*' * 20)
        funct()
        print('*' * 20)

    return wrapper


@decorated_with_lines
@decorated_with_stars
def original_function():
    print("Original Text...")



""" An example using *args """
def multiply_decorator(funct):
    def wrapper(*args):
        for arg in args:
            if (not isinstance(arg, int)) or (arg == 0):
                print("Invalid Input Entered...")
                return 
        
        return f"Result of '{funct.__name__}' is {funct(*args)}"

    return wrapper


@multiply_decorator
def original_function2(*args):
    n = 1
    for arg in args:
        n *= arg

    return n



""" Timer Example """
import time

def timer(funct):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = funct(*args, **kwargs)

        print(f"'{funct.__name__}' took {time.time() - start} seconds to run")
        
        return value
    return wrapper


@timer
def waste_some_time(times: int):
    counter = 0
    for number in range(times):
        counter += number



""" Decorator Parameters """
def prefix_decorator(prefix1, prefix2: str):
    def decorator(funct):
        def wrapper(*args, **kwargs):
            print(f"{prefix1}: Executed before '{funct.__name__}'", prefix2)
            value = funct(*args, **kwargs)
            print(f"{prefix1}: Executed after '{funct.__name__}'", prefix2)

            return value
        return wrapper
    return decorator


@prefix_decorator("Decorator Code", '!')
def show_name(name: str):
    print("Your name is " + name)



""" Creating a Class Decorator """
class Decorator_class:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args, **kwargs):
        print(f"Modidying '{self.funct.__name__}'...")

        return self.funct(*args, **kwargs)


@Decorator_class
def class_example():
    pass

class_example()
