"""
    Local -> Enclosing -> Global -> Built-in
"""

global_x = 10
print("Before Function Global X: " + str(global_x))


def for_local():
    local_y = 20
    print("Local Y: " + str(local_y))

    global global_x
    global_x = 20


for_local()
print("After Function Global X: " + str(global_x), '\n')


def outter():
    local_x = 5
    print("Before Inner Function local X: " + str(local_x))

    def inner():
        nonlocal local_x
        local_x = 10

    inner()
    print("After Inner Function Local X: " + str(local_x))


outter()
