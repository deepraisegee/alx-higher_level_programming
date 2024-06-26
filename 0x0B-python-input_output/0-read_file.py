#!/usr/bin/python3

"""Module that describe Input/Output"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, "r") as f:
        print(f.read())
