#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def save_to_json_string(my_obj, filename):
    """Write an object to a text file using  JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
