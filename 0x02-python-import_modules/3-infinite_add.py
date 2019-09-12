#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    argv = sys.argv
    i = 1
    count = 0
    if (len(argv) == 1):
        print("{:d}".format(count))
    else:
        while (i < len(argv)):
            count += int(argv[i])
            i += 1
        print("{:d}".format(count))
