#!/usr/bin/python3
"""Defines a rectangle class that inherits from Base."""
from base import Base


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
		"""	
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		super().__init__(id)

		@property
		def width(self):
			"""Gets the width."""
			return self.__width

		@width.setter
		def width(self, value):
			"""sets the width."""
			self.__width = value
		
		@property
		def height(self):
			"""Gets the height."""
			return self.__height

		@height.setter
		def height(self, value):
			"""sets the height."""
			self.__height = value
		
		@property
		def x(self):
			"""Gets the x coordinates."""
			return self.__x

		@x.setter
		def x(self, value):
			"""sets the x coordinates."""
			self.__x = value
		
		@property
		def y(self):
			"""Gets the y coordinates."""
			return self.__y
		


