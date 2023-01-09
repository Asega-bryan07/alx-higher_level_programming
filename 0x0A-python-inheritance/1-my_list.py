#!/usr/bin/bash/python3
"""A module that inherits from the list class"""

class MyList(list):
    """a class that inherits from the list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
