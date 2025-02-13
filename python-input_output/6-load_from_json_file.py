#!/usr/bin/python3
"""Module for load_from_json_file method."""


def load_from_json_file(filename):
    """Method for loading a JSON file."""
    import json

    with open(filename, 'r') as f:
        return json.load(f)
