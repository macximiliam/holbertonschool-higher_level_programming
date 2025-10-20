#!/usr/bin/python3
"""This module defines a function that checks if an object is an
instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        bool: True if obj inherits (directly or indirectly) from a_class,
              False if obj is an instance of a_class itself or unrelated.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
