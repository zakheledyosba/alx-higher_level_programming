#!/usr/bin/python3
"""Defines a text file-writing fuction."""


def write_file(filename="", text=""):
    """Write a string to the contents of a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
