#!/usr/bin/python3

"""More classes"""


def add_attribute(obj, prop, value):
    """adds a new attribute to an object if it’s possible
    Args:
        - obj
        - prop
        - value

    Return: None"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, prop, value)
