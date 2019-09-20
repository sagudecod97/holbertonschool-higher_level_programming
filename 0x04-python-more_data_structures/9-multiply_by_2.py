#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for elem in a_dictionary:
        new_dic[elem] = (a_dictionary[elem]) * 2

    return new_dic
