#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    length = len(matrix)

    if matrix == [] or matrix is None:
        return new_matrix

    for i in range(0, length):
        new_matrix.append([j ** 2 for j in matrix[i]])

    return new_matrix
