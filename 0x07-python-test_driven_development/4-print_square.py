#!/usr/bin/python3
def print_square(size):
    if size == None:
        raise TypeError("size must be an integer")

    if not type(size) == int and not type(size) == float:
        raise ValueError("size must be an integer")

    if type(size) == int and size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) == float:
        raise TypeError("size must be an integer")

    for i in range(int(size)):
        for j in range(int(size)):
            if (j == (size - 1)):
                print("#")
            else:
                print("#", end="")
