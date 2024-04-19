#!/usr/bin/python3

"""Module that describe Input/Output"""
import json


def from_json_string(my_str):
    """parse python object to JSON
    Args:
        - my_str

    Return: JSON representation of an object"""
    return json.loads(my_str)
