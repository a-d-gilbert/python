import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coordinator.Polar import Polar
from coordinator.Rectangular import Rectangular

class TestCoordinator(unittest.TestCase):

	def setUp(self):
		self.p_coord = (13, 22.6)
		self.r_coord = ()
		
	def test_setters(self):

	def test_conversion_functions(self):

