import math

class Polar:

    def __init__(self, p, angle_unit=0):
        self._angle_unit = angle_unit
        self.r = p[0]
        self.theta = p[1]
        self.point = p

    def angle_unit():
        doc = "the angular unit type"

        def fget(self):
            return self._angle_unit

        def fset(self, new_angle_unit):
            if(math.isnan(new_angle_unit)):
                raise TypeError('value set was not a number.')
            
            elif((new_angle_unit != 1) or (new_angle_unit != 0)):
                raise ValueError('value for angle_unit must be 1 or 0.')
            
            else:
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
            if(math.isnan(new_r)):
                    raise TypeError('Set value was not a number.')

            else:
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
            if(math.isnan(new_theta)):
                raise TypeError('Set value was not a number.')

            else:
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
            if(math.isnan(new_point[0]) or math.isnan(new_point[1]) ):
                raise TypeError('One of the tuple values was not a number.')
                    
            else:
                self._point = new_point

        def fdel(self):
            del self._point

        return locals()

    point = property(**point())

    @classmethod
    def from_rectangular(cls, rect, angle_unit=0):
        x = rect.x
        y = rect.y
        if(angle_unit == 0):
            if(x < 0 and y < 0):
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.atan(float(y/x)) + math.radians(180)
                
            elif(x < 0 and y > 0):
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.atan(float(y/x)) + math.radians(180)
                
            elif(x > 0 and y < 0):
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.atan(float(y/x)) + math.radians(360)
                
            else:
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.atan(float(y/x))

            return cls((r, theta))

        elif(angle_unit == 1):
            if(x < 0 and y < 0):
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.degrees(math.atan(float(y/x))) + 180
                
            elif(x < 0 and y > 0):
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.degrees(math.atan(float(y/x))) + 180
                
            elif(x > 0 and y < 0):
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.degrees(math.atan(float(y/x))) + 360
                
            else:
                r = math.sqrt((x ** 2) + (y ** 2))
                theta = math.degrees(math.atan(float(y/x)))
                
            return cls((r, theta))