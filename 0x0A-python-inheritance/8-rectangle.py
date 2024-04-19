#!/usr/bin/python3

"""Geometry class defination"""


class BaseGeometry:
    """Base class for Geometry"""

    def __init__(self, width, height):
        """Init method"""
        self.__width = width
        self.__height = height

    def area(self):
        """Area of Geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            - name
            - value

        Return: None"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
