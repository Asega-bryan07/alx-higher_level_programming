#!/usr/bin/bash/python3
"""defines a base geometry class BaseGeometry"""

class BaseGeometry:
    """the class that represents base geometry"""
    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates the value of an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
