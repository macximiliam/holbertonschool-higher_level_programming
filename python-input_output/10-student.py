#!/usr/bin/python3
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
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
