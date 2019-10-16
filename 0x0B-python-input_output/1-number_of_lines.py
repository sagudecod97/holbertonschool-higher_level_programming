#!/usr/bin/python3
def number_of_lines(filename=""):
    counter = 0

    with open(filename, encoding="utf-8") as f:
        for line in f:
            counter += 1

    return counter
