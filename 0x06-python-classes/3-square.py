#!/usr/bin/python3

"""This module contains a class that computes the area of a square"""


class Square:
    """This class finds the area of a square of size (size)
       field size must be an integer that is greater than or equal to 0
    """

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
