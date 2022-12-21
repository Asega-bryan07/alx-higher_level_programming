#!/usr/bin/python3

'''defines a class square'''
class Square:
    '''represents a square'''

	def __init__(self, size=0):
		if not isinstance(size, int):
			raise TypeError('size must be an integer')
		elif size < 0:
			raise ValueError('size must be >= 0')

		self.__size = size

	def are(self):
		'''
		calculate area of a square
		Returns the size of a square
		'''

		return (self.__size * self.__size)
