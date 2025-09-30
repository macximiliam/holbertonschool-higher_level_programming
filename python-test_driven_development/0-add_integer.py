#!/usr/bin/python3
"""
0-add_integer module
Adds two integers.
This module contains the add_integer function.
"""


def add_integer(a, b=98):
    """
    Add two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
