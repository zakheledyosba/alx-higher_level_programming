#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """create a python file from a JSON file."""
    return obj.__dict__
