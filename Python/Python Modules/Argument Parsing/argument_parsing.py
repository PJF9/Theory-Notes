import sys
import getopt
import os
import argparse


"""
To demonstrate how to `parse arguments` in Python we will set an example in which we 
will work with text files.

As the `first` argument we pass the full path of the file we want to open.
As the `second` argument to the program we pass the `mode`, meaning the action we want
to perform to the file.
Then after the `action` we pass the `message` that we want to write to the file if the
`writing` option is enabled.

We will refer 2 way to passing argument into a program, the first is using the module
'lib/getopt.py' and the second using 'lib/argparse.py'
"""


"""
We should notice that the first argument that we pass automaticly (when passing arguments)
is the name of the python file we are passing arguments to.
We can see all the arguments we are passing using 'sys.argv' that returns a List with the
our arguments.

The `first` way, using the module `getopt.py` we use the method 'getopt.getopt()' that 
requires 3 arguments. `First` the List of the arguments from 'sys.argv', then all the
optional arguments (that is passed using '-a' for argument) and are splitted using ':',
that denotes we will pass more infomrmation after '-a'
Finally as the `third` argument we are passing the equivelant name of '-a', etc it will
be '--argument', meaning that we can access '-a' using the name '--argument'
"""

opts, args = getopt.getopt(sys.argv[1:], "f:m:p:", ["filename", "message", "path"])

filename = ""
message = ""
path = os.getcwd()

for opt in opts:
    if opt[0] == '-f':
        filename = opt[1]
    elif opt[0] == '-m':
        message = opt[1]
    elif opt[0] == '-p':
        path = opt[1]

if filename != "" and path != "":
    with open(path + '\\' + filename + ".txt", 'a') as file:
        file.write(message)


"""
Using the module 'argparse.py' first we need to create an `argparse.ArgumentParser()` 

Then to add an argument we use the method 'add_argument()' that takes 4 argument.
The `first` argument is the equivelant to '-a' and the `second` the '--argument'
The `third` argument is a keyword argument named 'help' that denotes the use, the
purpose of this argument and finally another keyword argument `required` that tells
us that this argument is optional or not. 
If we want an argument to act only as a boolean we add the parameter 'action="store_true"'

After adding all the arguments, there are store inside a `Namespace`, so to convert it
into a `Dictionary` we us the function 'vars()'
"""

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filename", help="The name that the file will be written.", required=True)
parser.add_argument("-m", "--message", help="The message that will be written to the file", required=True)
parser.add_argument("-p", "--path", help="The path in which the file will be written.")

args = vars(parser.parse_args())

filename = "default_name.txt"
message = ""
path = os.getcwd()

for arg in args:
    if (arg == "filename") and (args[arg] is not None):
        filename = args[arg]
    elif (arg == "message") and (args[arg] is not None):
        message = args[arg]
    elif (arg == "path") and (args[arg] is not None):
        path = args[arg]

path = path + "\\" if not path.endswith("\\") else path

with open(path+filename, "w+") as file:
    file.write(message)
