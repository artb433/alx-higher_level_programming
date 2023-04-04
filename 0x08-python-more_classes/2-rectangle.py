#!/usr/bin/python3

"""
   this module creates a Rectangle class \
   that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """
       define a rectangle class and initialize with height and width
       find the area and perimeter of the rectangle

       if width or height is equal to 0, perimeter is equal to 0

       width must be an integer; else raise TypeError
       width must be >= 0; else raise ValueError

       height must be an integer; else raise TypeError
       height must be >= 0; else raise ValueError
    """

    def __init__(self, width=0, height=0):
        self.__height = 0
        self.__width = 0

        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        self.__height = value

        if not (isinstance(self.__height, int)):
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @width.setter
    def width(self, value):
        self.__width = value

        if not (isinstance(self.__width, int)):
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)
