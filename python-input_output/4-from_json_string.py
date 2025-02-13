#!/usr/bin/python3
"""Module for from_json_string method."""


def from_json_string(my_str):
    """Method for deserializing a string."""
    import json
    return json.loads(my_str)
