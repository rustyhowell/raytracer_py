import math

class Vec3:
    def __init__(self, e1, e2, e3):
        self.e0 = float(e1)
        self.e1 = float(e2)
        self.e2 = float(e3)

    @property
    def x(self):
        return self.e0

    @property
    def y(self):
        return self.e1

    @property
    def z(self):
        return self.e2

    @property
    def r(self):
        return self.e0

    @property
    def g(self):
        return self.e1

    @property
    def b(self):
        return self.e2

    def __add__(self, other):
        return Vec3(self.e0 + other.e0, self.e1 + other.e1, self.e2 + other.e2)

    def __sub__(self, other):
        return Vec3(self.e0 - other.e0, self.e1 - other.e1, self.e2 - other.e2)

    def __mul__(self, other):
        return Vec3(self.e0 * other.e0, self.e1 * other.e1, self.e2 * other.e2)

    def __div__(self, other):
        return Vec3(self.e0 / other.e0, self.e1 / other.e1, self.e2 / other.e2)

    @staticmethod
    def dot(v1, v2):
        return v1.e0 * v2.e0 + v1.e1 * v2.e1 + v1.e2 * v2.e2

    @staticmethod
    def cross(v1, v2):
        return Vec3(v1.e1 * v2.e2 - v1.e2 * v2.e1,
                    -1 * (v1.e0 * v2.e2 - v1.e2 * v2.e0),
                    v1.e0 * v2.e1 - v1.e1 * v2.e0)

    def squared_length(self):
        return self.e0 * self.e0 + self.e1 * self.e1 + self.e2 * self.e2

    def length(self):
        return math.sqrt(self.e0 * self.e0 + self.e1 * self.e1 + self.e2 * self.e2)

