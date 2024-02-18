#!/usr/bin/python3
"""
Inheriting Rectangle from Base
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculating area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displaying rectangle using symbols"""
        abscissa = " " * self.__x + "#" * self.__width + '\n'
        ordinate = '\n' * self.__y + abscissa * self.__height
        print(ordinate, end="")

    def __str__(self):
        """Changing toStr method"""
        rectId = "[Rectangle] ({})".format(self.id)
        rectPoses = "{}/{}".format(self.__x, self.__y)
        rectSizes = "{}/{}".format(self.__width, self.__height)
        return rectId + " " + rectPoses + " - " + rectSizes

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle instance."""
        if args:
            list_atr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Represent object as dictionary"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return {'x': x, 'y': y, 'id': id, 'height': h, 'width': w}
