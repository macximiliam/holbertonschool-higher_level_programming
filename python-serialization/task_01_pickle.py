#!/usr/bin/env python3
"""Module that defines a CustomObject class with pickle serialization."""

import pickle


class CustomObject:
    """A class that can be serialized and deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the attributes of the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a file and return a CustomObject instance."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except Exception:
            return None
