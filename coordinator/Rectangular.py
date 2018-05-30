import math

class Rectangular:

	def __init__(self, p):
		self.x = p[0]
		self.y = p[1]
		self.point = (self.x, self.y)

	def x():
		doc = "the x coordinate property"
		def fget(self):
			return self._x

		def fset(self, new_x):
			self._x = new_x

		def fdel(self):
			del self._x

		return locals()

	x = property(**x())

	def y():
		doc = "the y coordinate property"
		def fget(self):
			return self._y

		def fset(self, new_y):
			self._y = new_y

		def fdel(self):
			del self._y

		return locals()

	y = property(**y())

	def point():
		doc = "the point property"
		def fget(self):
			return self._point

		def fset(self, new_point):
			self._point = new_point

		def fdel(self):
			del self._point

		return locals()

	point = property(**point())

	@staticmethod
	def to_rectangular(p, angle_unit=0):
		r = p[0]
		theta = p[1]
		if(angle_unit == 0):
			x = r * math.cos(theta)
			y = r * math.sin(theta)
			return Rectangular((x,y))

		elif(angle_unit == 1):
			x = r * math.cos(math.radians(theta))
			y = r * math.sin(math.radians(theta))
			return Rectangular((x,y))
