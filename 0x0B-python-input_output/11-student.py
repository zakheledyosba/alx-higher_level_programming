#!/usr/bin/python3
"""Defines a class student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Get a dictionary representation of the Student.
            
            if attrs is a list of stringd, represents only those attributes
            included in the list
            """
            if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
        
        def reload_from_json(self, json):
            """Replace all attributes of the student
            
            Args:
                json (dict): The key pairs to replace attributes with.
            """
            for k, v in json.items():
                setattr(self, k, v)