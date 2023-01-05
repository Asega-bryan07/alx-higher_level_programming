#!/usr/bin/python3
"""THis defines a locked class"""

class LockedClass:
	"""Only allows instatiation of an attribute called first name"""
	__slots__ = ["first_name"]
