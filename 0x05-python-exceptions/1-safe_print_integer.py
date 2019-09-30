#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value != chr:
            print("{:d}".format(value))
            return True
        elif value.isdigit() == True:
            print("{:d}".format(int(value)))
            return True
    except:
        return False
