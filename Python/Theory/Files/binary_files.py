"""
Other than characters we can also store data in form of bytes. This can be done
by converting the data we want to write into bytes.

To declare that a file is binary, we add the suffix 'b' to the `mode` we want
the file to have (for 'r+' we use 'rb+').

For storing `complex` data types such us Lists and Dictionaries into a byte file we
use `json` files.
For String and Ints we can use the `build in` methods that Python provide us.
"""


"""
*                            Ints to Bytes (and Reversed)                              *

To store an intager 'x' into a byte file we need the method 'x.to_bytes()'
It takes 2 arguments: `first` the number of bytes we want to store 'x' and the `second`
argument is about where to store the MSB (We have 2 options 'big' for storing MSB to
the last byte and 'little' that stores MSB to the first bytes)

For example 'b = x.to_bytes(4, byteorder="big")' we are storing 'x' in 4 bytes with
MSB be stored to the last byte.

We should notice that the representation of `byte` data type in console is using
`hexadecimal` numbers. For example if 'x = 15' then when `printing` 'b' we see
'b'\x00\x00\x00\x0f''
This is acceptable because each `hexadecimal` number is stored in 4 bits, so 1 byte
consists 2 hexadecimal number, as we notice and also we see '\x0f' as the last byte
wich is the number 15, the MSB.

To convert a number from `byte` to `int` we use the method 'int.from_bytes()'
It takes 2 arguments: `first` the number is `byte` data type and then the `byteorder`
So by: 'int.from_bytes(b, byteorder="big")' we are getting 'x' back as an intager.
"""


"""
*                          Strings to Bytes (and Reversed)                            *

To store a String into `byte` we simply need to encode it. We do that using the method
'str.encode()'
We pass as argument the string we want to convert into bytes and we are done. So by 
writing 'b = str.encode(string)' we are converting 'string' into the `byte` 'b'

In representation in the console we see no difference, but by using the function 'type()'
we see that we have converted the String into Byte

For the reverse process we use the `byte` method 'decode()'
So by writing 'b.decode()' we have succesfully converted the `byte` string into a String.
"""

# Convertions
x = 20
b = x.to_bytes(4, byteorder="big")
print(b, type(b))
x = int.from_bytes(b, byteorder="big")
print(x, type(x))

s = "Peter Jacob"
b = str.encode(s)
print(b, type(b))
s = b.decode()
print(s, type(s))


# Writing a Binary File
int_list = [1, 2, 3]
string_list = ["Hi", " ", "there\n", "My\n", "name is Petros."]

with open("test.dat", "wb") as file:
    for num in int_list:
        file.write(num.to_bytes(4, byteorder="big"))
    
    for word in string_list:
        file.write(str.encode(word))


# Reading a Binary File
with open("test.dat", "rb") as file:
    for _ in range(len(int_list)):
        b = file.read(4)
        print(int.from_bytes(b, byteorder="big"))

    for i in range(len(string_list)):
        s = file.read(len(string_list[i]))
        print(s.decode())
