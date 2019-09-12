#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    argv = sys.argv
    i = 1
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        while (i < len(argv)):
            print("{:d}: {:s}".format((i), argv[i]))
            i += 1
