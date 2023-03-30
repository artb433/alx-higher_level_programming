#!/usr/bin/python3

"""This module flexes the power of OOP"""


class Square:
    """This class computes the area of a square

       self.__size is instantiated using getters and setters (size method)
       self.__size must be an integer greater than or equal to 0
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
