#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    maximum = max(zip(a_dictionary.values(), a_dictionary.keys(),))

    if maximum is 0:
        return None

    return maximum[1]
