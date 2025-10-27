#!/usr/bin/python3
"""Defines a class VerboseList that prints messages on list actions."""


class VerboseList(list):
    """List that shows messages when modified."""

    def append(self, item):
        """Add item to list and show message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Add several items and show message."""
        super().extend(iterable)
        print(f"Extend the list with [{len(iterable)}].")

    def remove(self, item):
        """Remove item and show message."""
        super().remove(item)
        print(f"Remove [{item}] from the list.")

    def pop(self, index=-1):
        """Remove item by index and show message."""
        item = super().pop(index)
        print(f"Popped [{index}] from the list.")
