#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = 0
if (number < 0):
    neg = (number * -1)
if (neg > 0):
    print("Last digit of {:d} is -{:d}".format(number, (neg % 10), end=" "))
else:
    print("Last digit of {:d} is {:d}".format(number, (number % 10)), end=" ")

if (number > 0 and (number % 10) > 5):
    print("and is greater than 5")
elif (((number % 10) == 0) and ((neg % 10) == 0)):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
