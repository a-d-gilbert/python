import math

class Point:

    RECTANGULAR = 2
    POLAR = 1
    RADIANS = 2
    DEGREES = 1

    def __init__(self, p, coord_type=1, angular_type=1):
        self.coord_type = coord_type
        self.angular_type = angular_type

        if(self.coord_type == Point.RECTANGULAR):
            self.x = p[0]
            self.y = p[1]
            self.rectangular = (self.x, self.y)
            self.polar = self.to_polar(self.rectangular)
            self.r = polar[0]
            self.theta = polar[1]

        elif(self.coord_type == Point.POLAR):
            self.r = p[0]
            self.theta = p[1]
            self.polar = (self.r, self.theta)
            self.rectangular = self.to_rectangular(self.polar)
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

    def to_polar(self, p):
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
        elif(self.angular_type == Point.DEGREES):
            if(p[0] < 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0]))) + 180
                return (r, theta)
            elif(p[0] < 0 and p[1] > 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0]))) + 180
                return (r, theta)
            elif(p[0] > 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0]))) + 360
                return (r, theta)
            else:
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0])))
                return (r, theta)

    def to_rectangular(self, p):
        if(self.angular_type == Point.RADIANS):
            x = p[0] * math.cos(p[1])
            y = p[0] * math.sin(p[1])
            return (x, y)

        else:
            x = p[0] * math.cos(math.radians(p[1]))
            y = p[0] * math.sin(math.radians(p[1]))
            return (x, y)
