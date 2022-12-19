#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Returns the division of a and b"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
