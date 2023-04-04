#!/usr/bin/python3

"""
   this module creates a Rectangle class \
   that defines a rectangle by: (based on 5-rectangle.py)
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

       str - returns a string of height and width of rectangle (using: #)
       repr - returns a string representation of the rectangle that can be;
              recreated with eval()

       del - print a message when an instance of Rectangle is deleted

       public class attribute: number_of_instances (initialized to 0)
       keeps track of number of class instances/objects
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__height = 0
        self.__width = 0

        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

    def __str__(self):
        string = ""

        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string = string + "#"

            if i != (self.__height - 1):
                string = string + "\n"

        return string

    def __repr__(self):
        string = "Rectangle({}, {})".format(self.__width, self.__height)
        return string

    def __del__(self):
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

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
