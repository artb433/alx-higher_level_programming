#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        i_len = len(i)

        for j in range(0, i_len):
            print("{:d}".format(i[j]), end="")

            if j != (i_len - 1):
                print(" ", end="")

        print()
