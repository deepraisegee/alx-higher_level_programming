#!/usr/bin/python3

"""Geometry class defination"""


class BaseGeometry:
    """Base class for Geometry"""

    def area(self):
        """Area of Geometry"""
        raise Exception("area() is not implemented")
