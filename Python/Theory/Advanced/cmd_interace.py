from subprocess import run
from os import getcwd


run("cls", shell=True)

user_input = None
while (user_input != "exit") and (user_input != "quit"):
    print()
    print(' <', getcwd(), '>')
    user_input = input(" $ ")

    output = run(user_input, shell=True, capture_output=True, text=True).stdout
    print(output[1:])
