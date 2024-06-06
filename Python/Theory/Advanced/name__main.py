"""
The condition 'if __name__ == "__main__"' is `True` if the code is being executed by the
file that is being `written`.

If a file `import` a file that has this condition then it `cannot` and it will not execute
the code that is under this condition. 

It's similar functionality with the 'main()' function in other `Programming Languages`
"""


def main():
    print(f"__name__ = {__name__}")


if __name__ == "__main__":
    main()
else:
    print(f"__name__ = {__name__}")
