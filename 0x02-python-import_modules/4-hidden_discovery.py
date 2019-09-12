#!/usr/bin/python3
import hidden_4
if (__name__ == "__main__"):
    array = dir(hidden_4)
    i = 1
    while (i < len(array)):
        if (not array[i].startswith("__")):
            print("{:s}".format(array[i]))
            i += 1
        else:
            i += 1
