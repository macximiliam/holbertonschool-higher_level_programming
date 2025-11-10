#!/usr/bin/env python3
"""Module for XML serialization and deserialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file"""
    # Create the root element
    root = ET.Element("data")

    # Add each key-value pair as a sub-element
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create the tree and write it to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a dictionary"""
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Create a dictionary from the XML elements
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
