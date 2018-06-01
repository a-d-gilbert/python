import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from coordinator import Polar as pol
#from coordinator import Rectangular as rect
from coordinator.Polar import Polar
from coordinator.Rectangular import Rectangular

c = (13, 22.6)
polar_point = Polar(c, 1)
rectangular_point = Rectangular.from_polar(polar_point)
polar_point = Polar.from_rectangular(rectangular_point, 1)

print(polar_point.r)
print(polar_point.theta)
print(polar_point.point)
print(polar_point.angle_unit)

print(rectangular_point.x)
print(rectangular_point.y)
print(rectangular_point.point)
