"""
colorama.Style.RESET_ALL => Reset's both foreground & background color
colorama.Fore.RESET      => Reset's foreground color
colorama.Back.RESET      => Reset's background color

The colors we can use:
    BLACK (default)
    BLUE
    CYAN
    GREEN
    LIGHTBLACK_EX
    LIGHTBLUE_EX
    LIGHTCYAN_EX
    LIGHTGREEN_EX
    LIGHTMAGENTA_EX
    LIGHTRED_EX
    LIGHTYELLOW_EX
    MAGENTA
    WHITE
    YELLOW

We can use all this colors either as foreground: 'Fore.color' or as backround: 'Back.color'
"""


import colorama

colorama.init()
print(" This is a normal text")

print(colorama.Fore.RED, "This is a red color text")
print(colorama.Fore.GREEN, "This is a red color text")
print(colorama.Fore.LIGHTYELLOW_EX, "This is a red color text")

print(colorama.Style.RESET_ALL)
print(colorama.Back.CYAN, "Text with cyan background")
