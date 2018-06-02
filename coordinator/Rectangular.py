import math
from decorators import rounded

class Rectangular:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	@property
	def x(self):
		"""the x coordinate property"""
		return self._x

	@x.setter
	@rounded
	def x(self, new_x):
		if(math.isnan(new_x)):
			raise TypeError('Set value was not a number.')

		else:
			self._x = new_x

	@x.deleter
	def x(self):
		del self._x


	@property
	def y(self):
		"""the y coordinate property"""
		return self._y

	@y.setter
	@rounded
	def y(self, new_y):
		if(math.isnan(new_y)):
			raise TypeError('Set value was not a number.')

		else:
			self._y = new_y

	@y.deleter			
	def y(self):
		del self._y

	@classmethod
	def from_polar(cls, polar):
		r = polar.r
		theta = polar.theta
		if(polar.angle_unit == 0):
			x = r * math.cos(theta)
			y = r * math.sin(theta)
			return cls(x, y)

		elif(polar.angle_unit == 1):
			x = r * math.cos(math.radians(theta))
			y = r * math.sin(math.radians(theta))
			return cls(x, y)
