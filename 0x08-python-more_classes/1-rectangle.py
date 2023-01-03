#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """This defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: represents width of the rectangle
            height:  represents height of the rectangle
            Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than zero"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            self.__height = value
