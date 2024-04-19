#!/usr/bin/python3

"""Instance cheking"""


def is_same_class(obj, a_class):
    """Check if an object is an instance
    Args:
        - obj
        - a_class

    Return: True or False"""
    return type(obj) is a_class
