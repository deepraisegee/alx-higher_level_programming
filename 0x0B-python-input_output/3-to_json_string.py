#!/usr/bin/python3

"""Module that describe Input/Output"""
import json


def to_json_string(my_obj):
    """parse python object to JSON
    Args:
        - my_obj

    Return: JSON representation of an object"""
    return json.dumps(my_obj)
