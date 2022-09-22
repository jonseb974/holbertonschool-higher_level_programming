#!/usr/bin/python3
# 2-matrix_divided.py
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Returns a new matrix (list of lists).
    the result of the matrix division is
    rounded to 2 decimal places
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
        for row in matrix:
            if len(row) == 0:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
        for nb in row:
            if type(nb) is not int and type(nb) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisonError("division by zero")

    new_matrix = [[round(nb / div, 2) for nb in row] for row in matrix]

    return new_matrix
