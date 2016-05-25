import math
from random import random


class Vec3:
    def __init__(self, e0, e1, e2):
        self.e0 = float(e0)
        self.e1 = float(e1)
        self.e2 = float(e2)

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

    def __eq__(self, other):
        return self.e0 == other.e0 and self.e1 == other.e1 and self.e2 == other.e2

    def __add__(self, other):
        return Vec3(self.e0 + other.e0, self.e1 + other.e1, self.e2 + other.e2)

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.e0 += other.e0
            self.e1 += other.e1
            self.e2 += other.e2
        else:
            self.e0 += other
            self.e1 += other
            self.e2 += other
        return self

    def __sub__(self, other):
        return Vec3(self.e0 - other.e0, self.e1 - other.e1, self.e2 - other.e2)

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.e0 -= other.e0
            self.e1 -= other.e1
            self.e2 -= other.e2
        else:
            self.e0 -= other
            self.e1 -= other
            self.e2 -= other
        return self

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(self.e0 * other.e0, self.e1 * other.e1, self.e2 * other.e2)
        else:
            return Vec3(self.e0 * other, self.e1 * other, self.e2 * other)

    def __imul__(self, other):
        if isinstance(other, self.__class__):
            self.e0 *= other.e0
            self.e1 *= other.e1
            self.e2 *= other.e2
        else:
            self.e0 *= other
            self.e1 *= other
            self.e2 *= other
        return self

    def __div__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(self.e0 / other.e0, self.e1 / other.e1, self.e2 / other.e2)
        else:
            return Vec3(self.e0 / other, self.e1 / other, self.e2 / other)

    def __idiv__(self, other):
        if isinstance(other, self.__class__):
            self.e0 /= other.e0
            self.e1 /= other.e1
            self.e2 /= other.e2
        else:
            self.e0 /= other
            self.e1 /= other
            self.e2 /= other
        return self

    def __repr__(self):
        return 'x={},y={},z={}'.format(self.e0, self.e1, self.e2)

    @staticmethod
    def cross(v1, v2):
        return Vec3(v1.e1 * v2.e2 - v1.e2 * v2.e1,
                    -1 * (v1.e0 * v2.e2 - v1.e2 * v2.e0),
                    v1.e0 * v2.e1 - v1.e1 * v2.e0)

    def squared_length(self):
        return self.e0 * self.e0 + self.e1 * self.e1 + self.e2 * self.e2

    def length(self):
        return math.sqrt(self.e0 * self.e0 + self.e1 * self.e1 + self.e2 * self.e2)


def unit_vector(v):
    m = max(math.fabs(v.e0), math.fabs(v.e1), math.fabs(v.e2))
    return v / m


def dot(this, other):
    return this.e0 * other.e0 + this.e1 * other.e1 + this.e2 * other.e2


def random_in_unit_sphere():
    while True:
        p = Vec3(random(), random(), random()) * 2.0 - Vec3(1, 1, 1)
        if dot(p, p) < 1.0:
            return p

def reflect(v, n):
    return v - n * dot(v, n) * 2.0