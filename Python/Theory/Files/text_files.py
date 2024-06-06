"""
`Text files` are files that only contains charachters. They are `storing` each character
into one single byte.

We can open a `text file` using the function 'opne()': file = open(file_name, mode)

The `modes` we can use are:
    r  : reading the file (default)
    w  : writting to the file
    a  : appending to the file
    r+ : both reading and writting

The function 'open()' returns an object, so Python has created some method to do our
job a lot eazier. Some of those are:
    close(), read(), readline(), readlines(), 
    write(), writelines(), seek(), tell(), truncate(),
    seekable(), readable(), writable(), 

close(): Closes `file` if i'ss open.

read(size): Returns a String with the 'size' bytes from `file` (default is -1: all bytes)

readline(size): Retrurns A String with `size` bytes from one line of `file` (default -1) and
    then proceeds to the next line.

readlines(size): Returns a List that contains the lines up to 'size' bytes of `file` (default -1)

write(bytes): Writes the 'bytes' into the file. 

writelines(list): Writes each byte stream from list into `file`

seek(offset, from): Sets the file position to 'offset' and returns the new position, (files,
    starts at offset 0 and each position is one character) starting from 'from' (default is
    0: start, 1: current position amd and 2: the end of the file)

tell(): Returns the current file position.

truncate(size): Resizes the file into 'size' bytes.

seekable(): Returns True if the file is seekable, otherwise False.

readable(): Returns True if `file` is readable, otherwise False.

writable(): Returns True if the file is writable, otherwise False.


The best way of opening a file is through a Contex Manager.
Other than 'read()' and 'readlines()' we can read the file using 'for line in file', and it will
return each iteration a line from the file, with the different that at the end of each line it will
also include '\n'
"""

file = open("file_1.txt", "w")
file.write("My name is Petros")
file.close()


# With Contex Manager
with open("file_2.txt", "w") as file:
    file.write("My name is Petros")
