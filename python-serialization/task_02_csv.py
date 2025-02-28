#!/usr/bin/env python3
""" Convert CSV to JSON """


import csv
import json


def convert_csv_to_json(csv_file):
    """ Convert CSV to JSON """
    data = []
    try:
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    except FileNotFoundError:
        print(f"File {csv_file} not found")
        return False
