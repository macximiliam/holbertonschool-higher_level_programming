#!/usr/bin/python3
"""This module provides a function to return the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list containing the names of the object's attributes and methods.
    """
    return dir(obj)
