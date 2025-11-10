#!/usr/bin/env python3
"""Basic serialization module - save and load JSON files."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a JSON file and deserialize it into a Python dictionary."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
