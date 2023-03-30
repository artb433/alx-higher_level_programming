#!/usr/bin/python3

"""Contains a Square class that initializes a private Square variable/field"""


class Square:
    """This class instantiates a private size field with the size parameter
       size must be an integer greater than or equal to 0
    """

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
