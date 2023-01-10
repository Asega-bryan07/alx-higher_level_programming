#!/usr/bash/python3

"""
Defines a rectangle subclass square
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square
    """
    def __init__(self, size):
        """
        Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
