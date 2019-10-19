#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Magic methods
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    """
    Setters and Getters
    """

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """
    Public methods
    """

    def update(self, *args, **kwargs):
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
        return {"id": self.id, "x": self.x, 'size':self.width, 'y': self.y}
