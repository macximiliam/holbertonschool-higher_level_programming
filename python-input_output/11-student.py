#!/usr/bin/python3
"""Defines a class Student for serialization/deserialization."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            # Create a new dict with only the attributes requested
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        # Return all attributes if attrs is None or invalid
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
