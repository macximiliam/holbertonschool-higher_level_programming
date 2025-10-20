#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a special type of rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square sides.
        """
        # Validate that size is a positive integer using BaseGeometry method
        self.integer_validator("size", size)

        # Store the size in a private attribute
        self.__size = size

        # Initialize parent (Rectangle) with equal width and height
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
