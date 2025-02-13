#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and save to a file """


import sys
import os

filename = "add_item.json"

try:
    import json
    if os.path.exists(filename):
        with open(filename, "r") as f:
            my_list = json.load(f)
    else:
        my_list = []
    my_list.extend(sys.argv[1:])
    with open(filename, "w") as f:
        json.dump(my_list, f)
except ImportError:
    pass
