from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Student:
    """
    Creating classes using the 'dataclass' decorator allowing Python to capture the
      functionality of the 'struct' container in other programming languages such as
      C/C++.
    """
    first_name: str
    last_name: str
    age: int
    majors: Optional[List[str]] = None
    grade: Optional[float] = None



def main():
    s1 = Student(first_name="Petros", last_name="Floratos", age=18, majors=["Math", "Copm. Science", "Physics"])



if __name__ == "__main__":
    main()

