#!/usr/bin/python3
"""This module defines the MyList class that inherits from list."""


class MyList(list):
    """A subclass of list with an additional method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list.

        This method uses the built-in sorted() function to display
        the list elements in ascending order.
        """
        print(sorted(self))
