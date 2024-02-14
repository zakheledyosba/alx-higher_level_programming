#!/usr/bin/python3
"""Defines a text file-appending fuction."""


def append_write(filename="", text=""):
    """Append a string to the contents of a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters append.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
