#!/usr/bin/python3
"""defines an empty rectangle"""


class Rectangle:
    """ represents an empty rectangle"""

    def __init__(self, width=0, height=0):
	"""initialises a new rectangle.
	Args:
	    width(int):the with of the new rectangle
	    height(int):the hieght of the rectangel.
	"""
	self.width = width
	self.__height = height

    @property
    def width(self):
	""" sets the width of the rectangle """
	return self.__width

    @width.setter
    def width(self, value):
    """ sets the width of the rectangle"""
	if not isinstance(value, int):
	   raise TypError("width must be an integer")
	elif value < 0:
	    raise ValueError("width must be >= 0")
	else:
	    self.__width = value

    @property
    def height(self):
    """retrives the height of the rectangle"""
	return self.__height

    @height.setter
    def height(self, value):
    """ set the value of the height """
	if not isinstance(value, int):
	    raise TypeError("height must be an integer")
	elif value < 0:
	    raise ValueError("height must be >= 0")
	else:
	    self.height = value        

    def area(self):
    """returns the area of the rectangle"""
	return (self.__width * self.__height)

    def perimeter(self):
    """ returns the rectangle perimeter"""
	if self.__width = 0 or self.__height = 0:
	    return (0)
	return ((self.__width * 2) + (self.__height *2))

    def __str__(self)
	""" return the printable representation of the rectangle"""
	if self.__width == 0 or self.__height == 0:
	    return ("")

	rect = []
	for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
