"""
Python is a dymanic language, so a python script doesn't get compiled and turned into a `.out` format, rather is gets
intepreted and can be ran as a python file.
Static Porgramming language, like C++, after creating a new variable to denote its `data type`.

The same functionality of denoting the `data type` of a variable is found in Python with the name `Type Hinting`.

The documentation can be found: https://docs.python.org/3/library/typing.html

In 3.10: typing.TypeAlias, typing.Self, Union as |
"""

from typing import Any, Union, Optional, List, Dict
from typing import Set, FrozenSet, DefaultDict, OrderedDict, ChainMap, Counter, Deque
from collections.abc import Sequence, Callable


####### Type Aliases (usefull for simplifying complex types) #######

# Example 1
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

print(scale(2.0, [1, 2]))

# Example 2
ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    """ ... """


####### Callable Type (usefull for denoting functions): `Callable[[Arg1Type, Arg2Type], ReturnType]` #######

# Example 1
def feeder(get_next_item: Callable[[], str]) -> None:
    """ ... """
def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    """ ... """


####### Any Type #######
a: Any = None

a = 9
a = [9]


####### Object Type (every type is a subtype of object) #######
def hash_a(item: object) -> int:
    """ ... """


####### Union (usefull when passing or returning different types) #######
def f(id: int, gpa: Union[int, float]) -> None:
    """ ... """


####### Optional (usefull for optional arguments) #######
def g(arg: Optional[int] = None) -> List[int]:
    """ ... """

def g(arg: Optional[str] = "PJ") -> Dict[str, int]:
    """ ... """
