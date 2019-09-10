#!/usr/bin/python3
for i in range(0, 9, 1):
    for j in range((0 + i + 1), 10, 1):
        if (i != 8 and j != 9):
            print("{:d}{:d},".format(i, j), end=" ")
        elif (i == 8 and j == 9):
            print("{:d}{:d}".format(i, j))
