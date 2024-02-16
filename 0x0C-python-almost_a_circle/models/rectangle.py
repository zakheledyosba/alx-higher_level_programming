#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
	"""Represents a rectangle."""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""Initalize the rectangle.

		Args:
			width (int): The width of the rectangle.
			height (int): The height of the rectangle.
			x (int): x coordinate from top-left corner of the rectangle.
			y (int): y coordinate from top-left corner of the rectangle.
			id : The id of the rectangele.Automatically assigned if None.

		Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
		"""	
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

		@property
		def width(self):
			"""Gets the width."""
			return self.__width

		@width.setter
		def width(self, value):
			"""sets the width."""
			if type(value) != int:
				raise TypeError("width must be an integer")
			if value <= 0:
				raise ValueError("width must be > 0")
			self.__width = value
		
		@property
		def height(self):
			"""Gets the height."""
			return self.__height

		@height.setter
		def height(self, value):
			"""sets the height."""
			if type(value) != int:
				raise TypeError("height must be an integer")
			if value <= 0:
				raise ValueError("height must be > 0")
			self.__height = value
		
		@property
		def x(self):
			"""Gets the x coordinates."""
			return self.__x

		@x.setter
		def x(self, value):
			"""sets the x coordinates."""
			if type(value) != int:
				raise TypeError("x must be an integer")
			if value <= 0:
				raise ValueError("x must be > 0")
			self.__x = value
		
		@property
		def y(self):
			"""Gets the y coordinates."""
			return self.__y
		
		@y.setter
		def y(self, value):
			"""sets the y coordinates"""
			if type(value) != int:
				raise TypeError("y must be an integer")
			if value <= 0:
				raise ValueError("y must be > 0")
			self.__y = value

		def area(self):
			"""Return the area of the rectangle."""
			return self.width * self.height
