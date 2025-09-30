#!/usr/bin/python3
"""
3-say_my_name module
This module provides a function that prints
a formatted name using first and last names.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
