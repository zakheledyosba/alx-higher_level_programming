#!/usr/bin/python3
"""Defines a Base class."""


class Base:
    """Represents a base class for other classes.
    
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instanace with an id.

        Args:
            id (int): The id of the instance.Automatically assigns a new id,if None.

        Attributes:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects