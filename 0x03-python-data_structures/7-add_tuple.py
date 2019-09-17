#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 1 and len(tuple_b) == 1):
        tuple_new = ((tuple_a[0] + tuple_b[0], 0))
    elif (len(tuple_a) == 1):
        tuple_new = ((tuple_a[0] + tuple_b[0]), 0 + tuple_b[1])
    elif (len(tuple_b) == 1):
        tuple_new = ((tuple_a[0] + tuple_b[0]), 0 + tuple_a[1])
    elif (len(tuple_b) == 0 and not len(tuple_a) == 0):
        tuple_new = (tuple_a[0], tuple_a[1])
    elif (len(tuple_a) == 0 and not len(tuple_b) == 0):
        tuple_new = (tuple_b[0], tuple_b[1])
    elif (len(tuple_a) == 0 and len(tuple_b) == 0):
        tuple_new = (0, 0)
    else:
        tuple_new = ((tuple_a[0] + tuple_b[0]), tuple_a[1] + tuple_b[1])

    return tuple_new
