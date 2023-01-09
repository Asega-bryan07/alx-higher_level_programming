#!/usr/bin/bash/python3
"""this module defines class MyInt that inherits from int"""

class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == operator with != behaviour"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
