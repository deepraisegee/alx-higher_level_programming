#!/usr/bin/python3

"""Module that describe Input/Output"""


def append_file(filename="", text=""):
    """append a string to a text file (UTF8) and
    returns the number of characters written:
    Args:
        - filename (str)
        - text (str)

    Return: size of string"""
    with open(filename, mode="a") as f:
        return f.write(text)
