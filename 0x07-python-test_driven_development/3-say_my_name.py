#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if first_name == None:
        raise TypeError("first_name must be a string")
    elif not type(first_name) == str:
        raise TypeError("first_name must be a string")

    if not type(last_name) == str:
        raise TypeError("last_name must be a string")
    elif last_name == None:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
