#!/usr/bin/python3
"""Module to convert to json string"""


def to_json_string(my_obj):
    """Converts a python object to a json string"""
    import json
    return json.dumps(my_obj)
