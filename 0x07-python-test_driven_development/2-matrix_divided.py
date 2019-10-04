#!/usr/bin/python3
def matrix_divided(matrix, div):
    array_length = 0
    count = 0
    j = 0
    count_arrays = 0
    ret_arr = []

    if type(matrix) == type(None) and type(div) ==type(None):
        return

    elif div == None:
        raise TypeError("div must be a number")

    if (len(matrix) == 1 and len(matrix[0]) == 0) or matrix == None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for array in matrix:
        if type(array) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        array_length += len(array)
        if (len(matrix[0]) != len(array)):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(array)):
            count += 1
            if (not type(array[i]) == int and not type(array[i]) == float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if (not type(div) == int and not type(div) == float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")


    for new_array in matrix:
        i = 0
        ret_arr.append([])
        for item in new_array:
            item = round(matrix[j][i] / div, 2)
            ret_arr[j].append(item)
            i += 1
        j += 1
    return ret_arr
