#!/usr/bin/python3
num1 = 0
num2 = 0

while (num1 <= 9):
    if (num2 < 9):
        print("{:d}{:d}, ".format(num1, num2), end=" ")
        num2 +=1
    elif (num2 == 9 and num1 < 9):
        print("{:d}{:d},".format(num1, num2), end=" ")
        num2 = 0
        num1 += 1
    elif (num2 == 9 and num1 == 9):
        print("{:d}{:d}".format(num1, num2))
        num1 += 1
