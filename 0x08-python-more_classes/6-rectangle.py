#!/usr/bin/python3
"""A module that describe a class"""


class Rectangle:
    """A simple class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructor method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """string representation"""
        text = ""
        for i, v in enumerate(range(self.height)):
            for j in range(self.width):
                text += "#"
            if i != self.height - 1:
                text += "\n"
        return text

    def __repr__(self):
        """String rep"""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """delete obj"""
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """the method to get the area of the rectangle class"""
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
