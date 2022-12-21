#!/usr/bin/python3

'''a module defining a square'''
class Square:
	def __init__(self, size=0):
		'''initializing the square class
		   Arg: size: represents size of the defined square
			Raises: TypeError: if the size is not integer
			       ValueError: if the size is less than zero
			       '''
	       if not isinstance(size, int):
		       raise TypeError('size must be an integer')
	       elif size < 0:
		       raise ValueError('size must be >= 0')

	       self.__size = size
