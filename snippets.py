# this is a file full of code I removed but might choose to implement elsewhere

from coordinator.Polar import Polar
from coordinator.Rectangular import Rectangular

@property
def point(self):
	"""the point property"""
	return self._point

@point.setter
@rounded
def point(self, new_point):
	if(math.isnan(new_point[0]) or math.isnan(new_point[1]) ):
		raise TypeError('One of the tuple values was not a number.')
		
	else:
		self._point = (new_point[0], new_point[1])

@point.deleter	
def point(self):
	del self._point

class DecoratorTest(object):

	def __init__(self, n):
		self.num = n

	def rounded(func):
		def wrapper(self, n):
			n = round(n, 2)
			func(self, n)

		return wrapper

	@property
	def num(self):
		return self._num

	@num.setter
	@rounded
	def num(self, val):
		self._num = val

dt = DecoratorTest(123.456)
print(dt.num)

def add_vector(v, w):
	x = v.x + w.x
	y = v.y + w.y
	rect = Rectangular(x, y)
	plr = Polar.from_rectangular(rect, 1)

	return rect, plr

