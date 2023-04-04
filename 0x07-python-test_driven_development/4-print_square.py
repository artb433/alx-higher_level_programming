#!/usr/bin/python3

"""
   This module contains a single function that prints a square

   The function has no return value
"""


def print_square(size):
    """
       print a square of length (size) and height (size)

       size must be an integer >= 0 /
       else raise TypeError
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
