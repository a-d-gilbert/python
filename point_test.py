#point test
from point import Point

coord = (13, 22.6)
p = Point(coord)

print(p.x)
print(p.y)
print(p.r)
print(p.theta)
print(p.rectangular)
print(p.polar)
print(p.to_polar(p.rectangular))
