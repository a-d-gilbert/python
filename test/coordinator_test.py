import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coordinator.Polar import Polar
from coordinator.Rectangular import Rectangular

class TestCoordinator(unittest.TestCase):

	def setUp(self):
		# self.p_in = (56, 27)
		# self.r_out = (49.90, 25.42)
		self.r_in = (23.50, -36.10)
		self.p_out = (43.08, 303.06)
		self.rect1 = Rectangular(self.r_in)
		self.pol1 = Polar(self.p_out, 1)

	def test_Rectangular_setters(self):
		with self.assertRaises(TypeError):
			self.rect1.x = 'wrong'# x
		with self.assertRaises(TypeError):
			self.rect1.y = 'wrong'# y
		with self.assertRaises(TypeError):
			self.rect1.point = ('wrong', 1)# rect point

	def test_polar_setters(self):
		with self.assertRaises(TypeError):
			self.pol1.r = 'wrong'# r
		with self.assertRaises(TypeError):
			self.pol1.theta = 'wrong'# theta
		with self.assertRaises(TypeError):
			self.pol1.point = ('wrong', 1)# polar point
		with self.assertRaises(TypeError):
			self.pol1.angle_unit = 'wrong'# angle unit
		with self.assertRaises(ValueError):
			self.pol1.angle_unit = 2# angle unit

	def test_conversion_functions(self):
		print(self.pol1.point)
		print(Polar.from_rectangular(self.rect1, 1).point)
		self.assertEqual(self.pol1, Polar.from_rectangular(self.rect1, 1))
		self.assertEqual(self.rect1, Rectangular.from_polar(self.pol1))

if __name__ == '__main__':
	unittest.main()