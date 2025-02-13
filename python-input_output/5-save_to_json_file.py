#!/usr/bin/python3
"""Module for save_to_json_file function."""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as f:
        import json
        f.write(json.dumps(my_obj))
