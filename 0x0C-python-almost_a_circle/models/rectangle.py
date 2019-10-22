#!/usr/bin/python3
""" Definition of the class Rectangle, that Inherits from the class Base"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle definition
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns the str representation of the class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of Height"""
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if not type(value) == int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if not type(value) == int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def display(self):
        """Displays a square of the width and height of the class"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print("", end=" ")
            for w in range(self.__width):
                if w == (self.__width - 1):
                    print("#")
                else:
                    print("#", end="")

    def update(self, *args, **kwargs):
        """Updates the values of the  class"""
        array = ["id", "width", "height", "x", "y"]

        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, array[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in array:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary returns a dict of the class' properties"""
        return ({'x': self.x, 'y': self.y, 'id': self.id, 
                'height': self.height, 'width': self.width})
