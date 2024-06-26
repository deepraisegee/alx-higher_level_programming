#!/usr/bin/python3

"""Base module for all module classes"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
