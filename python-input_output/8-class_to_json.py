#!/usr/bin/python3
"""Module to convert class objects to JSON-serializable dict
"""


def class_to_json(obj):
    return {key: value for key, value in vars(obj).items()
            if isinstance(value, (list, dict, str, int, bool))}
