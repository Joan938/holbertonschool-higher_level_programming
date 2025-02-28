#!/usr/bin/env python3
""" Basic serialization """

import json


def serialize_and_save_to_file(data, filename):
    """ Serialize data to JSON and save it to a file """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """ Load and deserialize data from a file """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
