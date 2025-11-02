#!/usr/bin/python3
"""Module that defines a function to convert a JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) from a JSON string"""
    return json.loads(my_str)
