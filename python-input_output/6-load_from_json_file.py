#!/usr/bin/python3
"""Module for loading Python objects from JSON files"""


import json


def load_from_json_file(filename):
    """Return the Python object stored in a JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
