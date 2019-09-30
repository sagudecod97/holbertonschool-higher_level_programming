#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        #sys.stderr.write(str(e))
        print(str(e), file=sys.stderr)
        return False

    return True
