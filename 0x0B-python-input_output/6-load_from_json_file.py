#!/usr/bin/python3

"""Module that describe Input/Output"""
import json


def load_from_json_file(filename):
    """parse python object to JSON
    Args:
        - filename

    Return: JSON representation of an object"""
    with open(filename, mode="r") as f:
        data = json.load(f)

    return data
