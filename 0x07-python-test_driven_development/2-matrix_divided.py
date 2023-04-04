#!/usr/bin/python3

"""
   module containing function to divide a matrix by a given number

   Return: a new matrix
"""


def matrix_divided(matrix, div):
    """
       divide the elements of a matrix by div

       div must be greater than 0; else raise ZeroDivisionError
       matrix must be a list of lists of type int or float; else /
       raise TypeError

       matrix must be a list of lists; else raise TypeError

       create new matrix and populate with the:
       results of division of given matrix

       EXAMPLE: new_matrix[0][0] = matrix[0][0] / div
       (rounded to 2 decimal places)
    """

    new_list = []
    new_matrix = []
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not (isinstance(matrix, list)):
        raise TypeError(err_msg)

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if not (isinstance(i, list)):
            raise TypeError(err_msg)

        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError(err_msg)

    length = len(matrix[0])

    for i in matrix:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for j in i:
            new_list.append(round(j / div, 2))

        new_matrix.append(new_list)
        new_list = []

    return new_matrix
