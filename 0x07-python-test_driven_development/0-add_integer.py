#!/usr/bin/python3

"""
This module supplies the function to add two integers
>>> add_integer(1, 2)
3
"""
def add_integer(a, b=98):
    """ Returns the add of a and b"""
    if (not type(a) == int and not type(a) == float) or a == None:
        raise TypeError("a must be an integer")
    elif (not type(b) == int and not type(b) == float) or b == None:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
