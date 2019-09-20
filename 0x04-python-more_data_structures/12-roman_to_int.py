#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str or roman_string is None):
        return (0)

    dictio = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    strLen = len(roman_string)
    ret = dictio[roman_string[strLen - 1]]

    for i in range(strLen - 1, 0, -1):
        cnt = dictio[roman_string[i]]
        prv = dictio[roman_string[i - 1]]
        if (prv >= cnt):
            ret += prv
        else:
            ret -= prv

    return ret
