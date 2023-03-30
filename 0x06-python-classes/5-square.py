#!/usr/bin/python3

"""This module performs some cool stuff with a Square class"""


class Square:
    """Find the area of a square
       self.__size must be an integer greater than or equal to 0

       print '#' size amount of times (considering both rows and cols)
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(self.__size, int):
            return TypeError("size must be an integer")

        if self.__size < 0:
            return ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")

            print()
