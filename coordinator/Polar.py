import math

class Polar:

    def __init__(self, p, angle_unit=0):
        self.angle_unit = angle_unit
        self.r = p[0]
        self.theta = p[1]
        self.point = (self.r, self.theta)

    def angle_unit():
        doc = "the angular unit type"

        def fget(self):
            return self._angle_unit

        def fset(self, new_angle_unit):
            self._angle_unit = new_angle_unit

        def fdel(self):
            del self._angle_unit

        return locals()

        angle_unit = property(**angle_unit())

    def r():
        doc = "The r property."

        def fget(self):
                    return self._r

        def fset(self, new_r):
                        self._r = new_r

        def fdel(self):
            del self._r

        return locals()

        r = property(**r())

    def theta():
        doc = "The theta property."

        def fget(self):
                return self._theta

        def fset(self, new_theta):
                self._theta = new_theta

        def fdel(self):
                del self._theta

        return locals()

    theta = property(**theta())

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
    def to_polar(p, angle_unit=0):
        if(angle_unit == 0):
            if(p[0] < 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0])) + math.radians(180)
                return Polar((r, theta))
            elif(p[0] < 0 and p[1] > 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0])) + math.radians(180)
                return Polar((r, theta))
            elif(p[0] > 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0])) + math.radians(360)
                return Polar((r, theta))
            else:
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.atan(float(p[1]/p[0]))
                return Polar((r, theta))
        elif(angle_unit == 1):
            if(p[0] < 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0]))) + 180
                return Polar((r, theta))
            elif(p[0] < 0 and p[1] > 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0]))) + 180
                return Polar((r, theta))
            elif(p[0] > 0 and p[1] < 0):
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0]))) + 360
                return Polar((r, theta))
            else:
                r = math.sqrt((p[0] ** 2) + (p[1] ** 2))
                theta = math.degrees(math.atan(float(p[1]/p[0])))
                return Polar((r, theta))