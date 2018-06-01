import math

class Rectangular:

	def __init__(self, p):
		self.x = p[0]
		self.y = p[1]
		self.point = p

	def x():
		doc = "the x coordinate property"
		def fget(self):
			return self._x

		def fset(self, new_x):
			if(math.isnan(new_x)):
				raise TypeError('Set value was not a number.')

			else:
				self._x = round(new_x, 2)

		def fdel(self):
			del self._x

		return locals()

	x = property(**x())

	def y():
		doc = "the y coordinate property"
		def fget(self):
			return self._y

		def fset(self, new_y):
			if(math.isnan(new_y)):
				raise TypeError('Set value was not a number.')

			else:
				self._y = round(new_y, 2)
						
		def fdel(self):
			del self._y

		return locals()

	y = property(**y())

	def point():
		doc = "the point property"
		def fget(self):
			return self._point

		def fset(self, new_point):
			if(math.isnan(new_point[0]) or math.isnan(new_point[1]) ):
				raise TypeError('One of the tuple values was not a number.')
				
			else:
				self._point = (round(new_point[0], 2), round(new_point[1], 2))
						
		def fdel(self):
			del self._point

		return locals()

	point = property(**point())

	@classmethod
	def from_polar(cls, polar):
		r = polar.r
		theta = polar.theta
		if(polar.angle_unit == 0):
			x = r * math.cos(theta)
			y = r * math.sin(theta)
			return cls((x,y))

		elif(polar.angle_unit == 1):
			x = r * math.cos(math.radians(theta))
			y = r * math.sin(math.radians(theta))
			return cls((x,y))
