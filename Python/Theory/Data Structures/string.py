"""
*                          Basic About Strings                                *
*                          Escape Characters                                  *
*                          String Indexing                                    *
*                          String Slicing                                     *
*                          Unpacking String Elements                          *   
*                          String Concatination (Without Methods)             *
*                          F-Strings                                          *
*                          Copying a List                                     *
*                          Converting to String                               *
*                          String Module                                      *
*                          String Methods                                     *
*                          String Functions                                   *

"""


"""
*                             Basic About Strings                                   *

A String is an `immutable` sequence of characters that are stored as an array of
`Unicode` bytes. We can see the number that is equivelant with a character 'c'
using 'ord(c)' (we can see the character that is equivelant to the number n
using 'chr(n)')

`Unicode` is reffered as the `encoding` method of matching a  unique character, 
let's say 'μ' into a sequence of 0s and 1s. Another method of encoding is `ASCII`,
that encodes only `engilsh` letetrs into binary.

Because internally String are arrays (just like Lists) it's and `ordered` data type.

We can create a string by `enclosing` the sequence of character we want to store
inside " ", ' ' for single line and in """ """ for multi line Strings.
"""


"""
*                              Escape Characters                                 *

Escape Characters are special characters that modifying how we see the string into
the console. Those are: 
    \'   : For the character '
    \"   : For the character "
    \\   : For the character |
    \n   : For new line
    \r   : For Cariege Return
    \t   : For inserting a tab
    \b   : For backspace
    \ooo : For octal representation (etc "\110\145\154\154\157" for "Hello") 
    \xhh : For Hex representation (etc "\x48\x65\x6c\x6c\x6f" for Hello)
"""


"""
*                            String Indexing                                     *

Because String and Lists are so much `alike` the same concepts that applies on
Lists also applies on String. 
"""


"""
*                              String Slicing                                      *

Because String and Lists are so much `alike` the same concepts that applies on
Lists also applies on String.
"""


"""
*                              Unpacking String Elements                             * 

The same concepts that applies on Lists regarding `unpacking` applies also on Strings
with the difference that the wildcard '*' returns a List with elements the letters
of the substring.
"""


"""
*                         String Concatination (Without Methods)                        *

The `same` concept that applies on Lists also applies on String.
"""


"""
*                                   F-Strings                                          *

F-String (formated String) gives us an `eazy` and `fast` way to inlcude values of
varibales into a String.

So far if we want to add the value of a variable 'x' in a String we could only use
`concatination`: 's = "x = " + str(x)', so if we want to add a lot of variables
into a string this syntax is getting a little messy.

The same String, using F-String get be written: 's = f"x = {x}"'

There are even more `powerfull`, because inside '{}' we can use some options that
`modify` the variable `behavior`.

If 'x' is a `real` number then we can use:  {x}, {x:a}, {x:a.b}
Where 'a' is the number of characters it will occupy (if has less it will fill with 0s)
and 'b' is the number of digits (including before decimal point) to be displayed.

If 'x' is an `intager` we can use another 3 options: {x:x}, {x:o}, {x:b}
Where 'x', 'o', 'b' are the hex, octal and binary `representation` of x.
"""


"""
*                                  Copying a List                                       *

String are `immutables` we don't have to use any special method to copy 2 String. We
can simply use the assignment operator: 's2 = s1'

Because they are immutables if we `expand` 's2', then 's1' will still be 's1', it will
not be also expanded.
"""


"""
*                                Converting to String                                    *

We `convert` any iterable that `contains` Strings as elements into a String using either
the method 'join()' or the function 'str()'

With 'join()' we first choose the `seperator` (etc "", " ", "*", String) and then as
parameters into the method the iterable we want to `convert` into String.
We should notice that if we want to `convert` a Dictionary into String, with way we are
converting only its `keys`.

With 'str()' we are enabling the `__str__()` dunder method of the iterable, so we are
getting the String as we are seeing it in console, when printing it.
"""


"""
*                                String Module                                      *

Python for another time come to the rescue with `string` module (import string)

Let's say we want all ASCII letters, then by simply using the the 'ascii_letters'
string from this module we are collecting in a String all those letters.

The functionality doesn't stop there. We also can use:
    string.ascii_letters   : All english letters.
    string.ascii_lowercase : Only lowercase english letters.
    string.ascii_uppercase : Only uppercase english letters.
    string.digits          : All natural numbers from 0 to 9.
    string.hexdigits       : All hex numbers from 0 to F.
    string.octdigits       : All octal numbers from 0 to 7.
    string.printable       : All printabe characters
    punctuation            : All punctuations (like !, @ and $)
    whitespace             : All whitespace characters
"""


"""
*                                  String Methods                                         *

Python has created a lot of methods to work with String. Those are:
    capitalize(), casefold(), center(), count(), encode(), endswith()
    expandtabs(), find(), format(), index(), isalnum(), isalpha(), isdecimal(),
    isdigit(), isprintable(), isspace(), istitle(), join(), ljust(),
    maketrans(), partition(), replace(), rjust(), split(), splitlines(),
    startswith(), strip(), swapcase(), title(), translate(), upper(),
    zfill()

    
capitalize(): Returns a String from `caller` with first character in uppercase and
    all the other into lowercase.

casefold(): This Returns a lowercase String from `caller. We also use 'lower()', but
    it works only for english characters. To see if a String is in lowercase we use
    'islower()'

center(l, c): Returns a cenetred String of 'l' length filled with 'c' for extra characters
    (default is ' ')

count(val, s, e): Return the number fo appearences of 'val' inside String starting from
    's'-index to ('e'-1)-index (defaults are 0 and length accordingly).

encode(enc): Returns the encoding a String using 'enc' encoding (default UTF-8)

endswith(val, s, e): Returns True if `caller` is ending in 'val', starting from 's'-index
    to ('e'-1)-index (defaults are 0 and length accordingly).

expandtabs(tabs): Sets the tabsize of the String into 'tabs'

find(val, s, e): Return the first index of 'val' in String, starting from 's'-index to
    ('e'-1)-index (defaults are 0 and length accordingly). Will return `-1` if 'val'
    doen not exists. Use 'rfind()' if you want the last appearence.

index(val, s, e): Return the first index of 'val' in String, starting from 's'-index to 
    ('e'-1)-index (defaults are 0 and length accordingly). Will raise error if 'val' does
    not exists. Use 'rindex()' for the last appearence.

isalnum(): Returns True if all characters in the String are alphanumeric.

isalpha(): Returns True if all characters in the String are in the english alphabet.

isdecimal(): Returns True if all characters in the String are decimals (0-9).

isdigit(): Returns True if all characters in the String are digits.

isprintable(): Returns True if all characters in the String are printable.

isspace(): Returns True if all characters in the String are whitespaces.

istitle(): Returns True if the String follows the rules of a title.

sep.join(iterable): Joins the elements 'iterable' to a string with 'sep' as seperator.

ljust(l, c): Returns a length 'l' String from `caller` where extra characters 'c' are
    being placed to the right.

rjust(l, c): Returns a length 'l' String from `caller` where extra characters 'c' are
    being placed to the left.

partition(val): Returns a Tuple where the String is parted into three parts according to the
    first appearence of 'val' ('val' will be the second part). Use 'rpartition()' if you
    want the partition to be base on tha last 'val'

replace(old, new, c): Returns a String where a specified value is replaced with a specified
    value and will replace 'c' total olds.

split(sep, c): Returns a List that contains the splitted String base on the the first 'sep'
    appearence ('sep' will not be concluded). The second argument is how many splits we want
    to do. Use 'rsplit()' to start from the end of the String.

splitlines(keppline): Returns a List that contains the lines of the string. If 'keepline' is
    True the '\n' will be inluded, otherwise not.

startswith(val, s, e): Similar to 'endswith()' but returns True if String starts with 'val'

strip(chars): Returns a String that is created from `caller` if we delete all rigth and left
    spaces. If 'chars' specified, then we trim all the left and right characters from 'chars'
    User 'lstrin()' to remove only left chars and 'rstrip()' to remove only right chars.

swapcase(): Changes the case off each letter.

title(): Converts the first character of each word to upper case.

upper(): This Returns an uppercase String from `caller. To see if a String is uppercase we use
    'isupper()'

zfill(len): Fills the string with a specified number of values at the beginning. The total
    String is going to have size 'len'

format(*vals): see https://www.w3schools.com/python/ref_string_format.asp

translate(): https://www.w3schools.com/python/ref_string_translate.asp

maketrans(): https://www.w3schools.com/python/ref_string_maketrans.asp
"""
