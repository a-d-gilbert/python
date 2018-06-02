import math
from decorators import rounded

class Polar:

    def __init__(self, r, theta, angle_unit=0):
        self._angle_unit = angle_unit
        self.r = r
        self.theta = theta

    @property
    def angle_unit(self):
        """the angular unit type"""
        return self._angle_unit

    @angle_unit.setter
    def angle_unit(self, new_angle_unit):
        if(math.isnan(new_angle_unit)):
            raise TypeError('value set was not a number.')
        
        elif((new_angle_unit != 1) or (new_angle_unit != 0)):
            raise ValueError('value for angle_unit must be 1 or 0.')
        
        else:
            self._angle_unit = new_angle_unit

    @angle_unit.deleter
    def angle_unit(self):
        del self._angle_unit

    @property
    def r(self):
        """The r property."""
        return self._r

    @r.setter
    @rounded
    def r(self, new_r):
        if(math.isnan(new_r)):
                raise TypeError('Set value was not a number.')

        else:
            self._r = new_r

    @r.deleter
    def r(self):
        del self._r

    @property
    def theta(self):
        """The theta property."""
        return self._theta

    @theta.setter
    @rounded
    def theta(self, new_theta):
        if(math.isnan(new_theta)):
            raise TypeError('Set value was not a number.')

        else:
            self._theta = new_theta

    @theta.deleter
    def theta(self):
        del self._theta

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

            return cls(r, theta)

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
                
            return cls(r, theta, angle_unit)