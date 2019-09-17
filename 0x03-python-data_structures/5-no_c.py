#!/usr/bin/python3
def no_c(my_string):
    i = 0
    trans = {67: None, 99: None}
    string = my_string.translate(trans)
    return (string)
