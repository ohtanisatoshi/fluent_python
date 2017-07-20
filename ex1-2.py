from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(x=%r, y=%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scaler):
        return Vector(self.x * scaler, self.y * scaler)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1+v2)
v3 = Vector(3, 4)
v4 = Vector(5, 6)
print(abs(v3))
print(abs(v4))
