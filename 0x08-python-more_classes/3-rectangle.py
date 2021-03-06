#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        returnStr = ""

        if self.__width == 0 or self.__height == 0:
            returnStr = ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    if j == self.__width - 1 and i != self.__height - 1:
                        returnStr += "#\n"
                    elif j == self.__width - 1 and i == self.__height - 1:
                        returnStr += "#"
                    else:
                        returnStr += "#"

        return returnStr

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        areaResult = self.__width * self.__height
        return areaResult

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter
