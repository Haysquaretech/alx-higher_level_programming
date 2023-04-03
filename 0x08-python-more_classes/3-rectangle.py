#!/usr/bin/python3
""" more practice on classes!!! """


class Rectangle:
    """ initializes with the width and height with value check

    Args:
        width: how fat this 4polygon gonna be
        height: how tall is the box

    Return: nonezo
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width


@width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the area of this rekt """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of this rectangle """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width) * 2 + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i is not self.__height - 1:
                string += "\n"
        return string

     """ Not needed right here. only later
    def __repr__(self):
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        return string
    """
