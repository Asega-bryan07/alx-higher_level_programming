#!/usr/bin/python3

"""
This module defines a string-to-JSON function
""" 


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
