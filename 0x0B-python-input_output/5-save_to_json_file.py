#!/usr/bin/python3

"""Module that describe Input/Output"""
import json


def save_to_json_file(my_obj, filename):
    """parse python object to JSON
    Args:
        - my_obj
        - filename

    Return: JSON representation of an object"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
