#!/usr/bin/python3
""" Definition of class Square that inherits of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Definition of the class Squeare
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the str representation of the class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """Returs the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the value of the class"""
        array = ["id", "size", "x", "y"]

        if not len(args) == 0:
            for i in range(len(args)):
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                else:
                    setattr(self, array[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in array:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the class"""
        return {"id": self.id, "x": self.x, 'size': self.width, 'y': self.y}
