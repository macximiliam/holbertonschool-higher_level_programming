#!/usr/bin/python3
"""Module that defines a function to convert an object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
