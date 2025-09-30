#!/usr/bin/python3
"""
4-print_square module

This module provides a function that prints a square
with the character '#', based on the given size.
"""


def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
