#!/usr/bin/python3

class square:
        '''a class that represents a square'''
        def __init__(self, size=0):
                if isinstance(size, int):
                        raise TypeError('size must be an integer')
                if size < 0:
                        raise ValueError('size must be >= 0')

                self.__size = size

        @property
        def size(self):
                '''gives the size of a square'''

                return self.__size

        @size.setter
        def size(self, value):
                if not isinstance(value, int):
                        raise TypeError('size must be an integer')
                if size < 0:
                        raise ValueError('size must be >= 0')
        self.__size = value

        def area(self):
                '''
                calculate area of the square
                Returns: The size of the square
                '''
                return (self.__size ** 2)
	def my_print(self):
		'''print the square in #'''

		if self.__size == 0:
			print()

			for i in range(self.__size):
				print('#' * self.__size)
