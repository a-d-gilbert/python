import math

class Point:
   RECTANGULAR = 2
   POLAR = 1
   RADIANS = 2
   DEGREES = 1

   def __init__(self, p, coord_type=2, angular_type=2):
      self.coord_type = coord_type
      self.angular_type = angular_type

      if(self.coord_type == Point.RECTANGULAR):
         self.x = p[0]
         self.y = p[1]
         self.rectangular = (self.x, self.y)
         self.polar = to_polar(p)
         self.r = self.polar[0]
         self.theta = self.polar[1]

     elif(self.coord_type == Point.POLAR):
         self.polar = (p[0], p[1])
         self.r = p[0]
         self.theta = p[1]
         self.rectangular = to_rectangular(self.polar)
         self.x = self.rectangular[0]
         self.y = self.rectangular[1]


    def rectangular():
        doc = "The rectangular property."
        def fget(self):
            return self._rectangular
        def fset(self, value):
            self._rectangular = value
        def fdel(self):
            del self._rectangular
        return locals()
    rectangular = property(**rectangular())

    def polar():
        doc = "The polar property."
        def fget(self):
            return self._polar
        def fset(self, value):
            self._polar = value
        def fdel(self):
            del self._polar
        return locals()
    polar = property(**polar())

    def x():
        doc = "The x property."
        def fget(self):
            return self._x
        def fset(self, value):
            self._x = value
        def fdel(self):
            del self._x
        return locals()
    x = property(**x())

    def y():
        doc = "The y property."
        def fget(self):
            return self._y
        def fset(self, value):
            self._y = value
        def fdel(self):
            del self._y
        return locals()
    y = property(**y())

    def r():
        doc = "The r property."
        def fget(self):
            return self._r
        def fset(self, value):
            self._r = value
        def fdel(self):
            del self._r
        return locals()
    r = property(**r())

    def theta():
        doc = "The theta property."
        def fget(self):
            return self._theta
        def fset(self, value):
            self._theta = value
        def fdel(self):
            del self._theta
        return locals()
    theta = property(**theta())

    def to_polar(p):
        if(self.angular_type == Point.RADIANS):
            if(p[0] < 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0])) + math.radians(180)
                return (r, theta)
            elif(p[0] < 0 and p[1] > 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0])) + math.radians(180)
                return (r, theta)
            elif(p[0] > 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0])) + math.radians(360)
                return (r, theta)
            else:
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0]))
                return (r, theta)

    def to_rectangular(p):
        if(self.angular_type == Point.RADIANS):
            x = p[0] * math.cos(p[1])
            y = p[0] * math.sin(p[1])
            return (x, y)

        else:
            x = p[0] * math.degrees(math.cos(math.radians(p[1])))
            y = p[0] * math.degrees(math.sin(math.radians(p[1])))
            return (x, y)
