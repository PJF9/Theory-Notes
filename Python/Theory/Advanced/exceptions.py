"""
When an `error` occur in our program Python creates an `exception` object and it
`throw`s it to us, meaning it's been `appearing` in the termnial and the program
`stops` execution.

Each error consists of 3 parts, the `traceback`, the `error type` and the `decription`
Traceback is the recursive printing of all the functions that envolves the error so
the programmer can spot it eazily.
Error type is the category of the error, we will discuss later on.
And lastly description is some text to give more clarity to the programmer about the
error.

Of course Python has provided us a way to handle and `catch` a potential error.
Syntax:
	try:
		...
	except (error1, error2, ...):
		...
	else:
		...
	finally:
		...

try: We place all the suspicious code.

except: Catching the errors. When an error occur Python will stop the `try` execution
	and will search at the `catch` section to find the specific error type.

else: Runs if the code inside `try` didn't raise eny errors.

finally: Runs always, either after `else` (if we didn't return to stop the function
	execution) or after `catch` if an error occur.

In fact we have a lot of `catching` capabilities:
1) For catching all error types:
	- exept:
		...	
	- except Exception [as e]:
		...

	`Exception` is the Base class for most of exception (error) types.

2) For catching a specific error type, for example `IndexError`:
	- except IndexError [as e]:
		...

3) For catching more that one errors:
	- except Error1 [as e1]:
		...
	  except Error2 [as e2]:
		...
	  ...
	
	When an error occur inside `try` then sequencialy Python searches for the `except`
	statement that `handles` this specific error. If no such `except` block exixst it
	will throw the error as it is reasonable.
	
There are a lot of `Exception Types`. In fact there is a `hierarchy` of excetpion classe
with first `Base` the class `BaseException`
Some derived classes of BaseException are `Exception` and `KeyboardInterrupt`
Then some children of Exception are `ArithmeticError` (which is the Base of `ZeroDivisionError`
and `OverflowError`), `AttributeError`, `ImportError` (which is the Base of `ModuleNotFoundError`),
`LookupError` (which is the parent of `IndexError` and `KeyError`)

KeyboardInterrupt: Pressing 'Ctrl + C' (or Del) at runtime.
ZeroDivisioError: Dividing by 0.
OverflowError: Storing a 'VERY' large number in memory.
AttributeError: Non existing attribute.
ImportError: Importing a module that doesn't exist.
IndexError: Reach an invalid index position.
KeyError: Non existing Dictionary key.
MemoryError: Messing with memory.
RecursionError: Reaching maximum recrusion depth.
ValueError: Receiving an argument to a function that has the correct type but
	inappropriate value.
TypeError: Applying a function to an object of inappropriate type.
FileNotFoundError: Non existing file.
StopIteration: Reaching the end of 'next()' method.
IndentationError: Indentating incorrect.

The full list of tha class `hierarchy`: https://docs.python.org/3/library/exceptions.html


Python privide us a way to `causing` an exception if we want. We can do that using the
keyword 'raise' following with the exception type.

Inheriting from any exception class we can `create` our own exception types.
"""


# Creating our own exceptions
class My_Exception(Exception):
	def __init__(self, val, message):
		self.val = val
		self.message = message

	def __str__(self):
		return f"{self.message}: {self.val} is not valid"
	
class CustomKeyInterrupt(KeyboardInterrupt):
	def __str__(self):
		return "Custom KeyboardInterrupt..."

try:
	num = 10
	if num > 2:
		raise My_Exception(num, "Invalid Value")
except My_Exception as ex:
	print(ex)


# Catching CustomKeyInterrupt
try:
	while True:
		x = input("> ")
except KeyboardInterrupt:
	try:
		raise CustomKeyInterrupt
	except CustomKeyInterrupt as obj:
		print(obj)
