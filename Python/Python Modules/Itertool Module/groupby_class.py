from itertools import groupby

"""
    This method works with iterables that have key value pair
    The only think it does is that is group the data by a specific key

    First we need a function that returns the key we want the iterable to group the data
    Then we need to create the data in a form of key value pairs

    Arguments:
    1. The iterable
    2. The function that we built earlier ( can also make a lamda function )
"""

#? Example

def group_persons_by(person):
    return person["major"]

persons = [
    {"name": "Petros Floratos", "age": 17, "major": "Comp. Science"},
    {"name": "Jacob Floratos", "age": 19, "major": "Comp. Science"},
    {"name": "Tony Floratos", "age": 17, "major": "Comp. Science"},
    {"name": "Joe Doe", "age": 20, "major": "Chemistry"},
    {"name": "Dane Doe", "age": 18, "major": "Math"},
    {"name": "John Smith", "age": 18, "major": "Math"},
    {"name": "Lina Agent", "age": 22, "major": "Math"}
]

grouped_persons = groupby(persons, group_persons_by)

for key, group in grouped_persons:
    print("---------------------")
    print(f"Major: {key}")
    print("---------------------")
    for person in group:
        print("*", person["name"], person["age"])
    
    print("\n")
