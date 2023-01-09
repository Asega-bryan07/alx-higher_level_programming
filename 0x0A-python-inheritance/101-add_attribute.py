#!/usr/bin/bash/python3
"""This module defines a function that adds a new attribute to an object"""

def add_attribute(obj, att, value):
    """adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    setattr(obj, att, value)
