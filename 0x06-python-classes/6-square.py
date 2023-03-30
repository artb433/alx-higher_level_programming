#!/usr/bin/python3

"""Again, another function that does cool stuff with a Square class"""


class Square:
    """print a square using # (by size amount of times)

       self.__size must be an integer >= 0
       self.__position is a tuple of two integers that must be >= 0
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(self.__size, int):
            return TypeError("size must be an integer")

        if self.__size < 0:
            return ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        err_msg = "position must be a tuple of 2 positive integers"
        self.__position = value

        if len(self.__position) != 2:
            raise TypeError(err_msg)

        for i in range(2):
            if not isinstance(self.__position[i], int):
                raise TypeError(err_msg)
            if self.__position[i] < 0:
                raise TypeError(err_msg)

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            if not self.__position[1] > 0:
                for i in range(self.__position[0]):
                    print(" ", end="")

            for i in range(self.__size):
                print("#", end="")

            print()
