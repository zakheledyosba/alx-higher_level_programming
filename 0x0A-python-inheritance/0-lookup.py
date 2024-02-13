#!/usr/bin/python3
"""Difine an object attribute lookup fuction"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return (dir(obj))
