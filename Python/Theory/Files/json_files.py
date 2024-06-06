"""
JSON (JavaScript Object-Notation) is a way of `storing` both simple data like Ints and Strings
but also more `complex` ones, like Lists and Dictionaries. 
It's a `tool` that has created in JavaScript and we can access it in Python using the module `json`

To store data in `files` using JSON we need first to convert them into JSON `objects` and for reading
them from the file we need through JSON to convert them againg into Python objects.

With JSON we are storing all data into a single line (we can change that with the keyword argument
`index`)

We can convert 'x' to a JSON object we use the method 'json.dumps(x)'

To store, let's say, a Dictionary 'd' into a `file` 'f' we use: 'json.dump(d, f)'
This method can take 3 keyword arguments:
1) indent: A number that tells us the number of indentation.
2) sort_keys: True if we want to sort the `keys`, otherwise False.
3) separators: Its a Tuple with 2 elements: first the replacement of ',' and then the replacement of ':'

We can read from a JSON `file` 'f' using 'json.loads(f)' 
""" 

import json

List = [1,2,3,4,5]

with open("file_5.json", "w") as file:
    json.dump(List, file)
    file.write("\n")
    json.dump({"1": 1, "2": 2, "3": 3}, file)
    file.write("\n")
    json.dump("Hallo There Sir", file)
    file.write("\n")


with open("file_5.json", "r") as file:
    for line in file:
        print(json.loads(line))
