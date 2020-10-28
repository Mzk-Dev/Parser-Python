class Building:

	def __init__(self, south, west, width_WE, width_NS, height=10):
		self.__south = south
		self.__west = west
		self.__width_WE = width_WE
		self.__width_NS = width_NS
		if height <= 0:
			self.__height = 10
		else:
			self.__height = height

	def corners(self):
		cor = {}
		cor['north-west'] = [self.__south + self.__width_NS, self.__west]
		cor['north-east'] = [self.__south + self.__width_NS, self.__west + self.__width_WE]
		cor['south-west'] = [self.__south, self.__west]
		cor['south-east'] = [self.__south, self.__west + self.__width_WE]
		return cor

	def area(self):
		return self.__width_WE * self.__width_NS

	def volume(self):
		return self.area() * self.__height

	def __repr__(self):
		return f'Building({self.__south}, {self.__west}, {self.__width_WE}, {self.__width_NS}, {self.__height})'



if __name__ == '__main__':
    import doctest
    doctest.testmod()

