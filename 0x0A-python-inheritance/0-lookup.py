#!/usr/bin/python3

"""
a module that returns the list of available attributes and methods
of an object
"""

def lookup(obj):
    """
    the function looks for all attributes and methods of an object
    """
    return dir(obj)
