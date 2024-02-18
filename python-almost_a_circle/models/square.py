#!/usr/bin/python3
"""
Inheriting Square from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of object"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """toStr method"""
        sId = "[Square] ({}) ".format(self.id)
        return sId + "{}/{} - {}".format(self.x, self.y, self.size)

    @property
    def size(self):
        """Size getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square instance."""
        if args:
            list_atr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Represent object as dictionary"""
        id = self.id
        s = self.__width
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': s, 'y': y}
