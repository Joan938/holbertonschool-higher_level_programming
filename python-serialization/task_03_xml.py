#!/usr/bin/env python3
""" 3. XML """
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serializes a dictionary to XML """
    root = ET.Element("data")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """ Deserializes an XML file to dictionary """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {element.tag: element.text for element in root}
