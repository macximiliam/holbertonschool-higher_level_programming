#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a special type of rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        # Validate that size is a positive integer
        self.integer_validator("size", size)

        # Store size as a private attribute
        self.__size = size

        # Call the parent class constructor (Rectangle)
        # Since a square is a rectangle with equal width and height
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
