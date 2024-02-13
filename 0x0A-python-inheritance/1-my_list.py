#!/usr/bin/python3
"""Difines an inherited list class MyList."""


class MyList(list):
    """Impliments sorted printing for built-in list class."""

def print_sorted(self):
        """Print a sorted list in ascending order."""
        print(sorted(self))
