#!/usr/bin/python3

"""Module that describe Input/Output"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written:
    Args:
        - filename (str)
        - text (str)

    Return: None"""
    with open(filename, mode="w") as f:
        return f.write(text)
