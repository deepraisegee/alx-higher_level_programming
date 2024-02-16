#!/usr/bin/python3
"""
A file for an empty class that defines a square.
"""


class Square:
    """A class that defines a sqaure"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get the area of the square instance"""
        return self.__size ** 2

    def my_print(self):
        """print square to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
