import unittest
import math
from vector3 import Vec3

class TestVec3(unittest.TestCase):

    def test_init(self):
        v1 = Vec3(1, 2, 3)
        self.assertEqual(v1.r, 1.0)
        self.assertEqual(v1.g, 2.0)
        self.assertEqual(v1.b, 3.0)

    def test_length(self):
        v = Vec3(1, 2, 3)
        self.assertEqual(v.length(), math.sqrt(14.0))

        v = Vec3(1, 2, -3)
        self.assertEqual(v.length(), math.sqrt(14.0))

    def test_squared_length(self):
        v = Vec3(1, 2, 3)
        self.assertEqual(v.squared_length(), 14.0)

        v = Vec3(1, -2, 3)
        self.assertEqual(v.squared_length(), 14.0)

    def test_add(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(10, 20, 30)
        v3 = v1 + v2
        self.assertEqual(v3.r, 11)
        self.assertEqual(v3.g, 22)
        self.assertEqual(v3.b, 33)

        self.assertEqual(v1.r, 1)

    def test_iadd(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(10, 20, 30)
        v1 += v2
        self.assertEqual(v1.r, 11)
        self.assertEqual(v1.g, 22)
        self.assertEqual(v1.b, 33)

        self.assertEqual(v2.r, 10)
        self.assertEqual(v2.g, 20)
        self.assertEqual(v2.b, 30)

    def test_sub(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(10, 20, 30)
        v3 = v2 - v1
        self.assertEqual(v3.r, 9)
        self.assertEqual(v3.g, 18)
        self.assertEqual(v3.b, 27)

        self.assertEqual(v1.r, 1)
        self.assertEqual(v2.r, 10)

    def test_isub(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(10, 20, 30)
        v2 -= v1
        self.assertEqual(v2.r, 9)
        self.assertEqual(v2.g, 18)
        self.assertEqual(v2.b, 27)

        self.assertEqual(v1.r, 1)
        self.assertEqual(v1.g, 2)
        self.assertEqual(v1.b, 3)

    def test_sub_vec(self):
        v = Vec3(1, 2, 3)
        v2 = Vec3(3, 4, 5)
        v3 = v * v2
        self.assertEqual(v3.r, 3)
        self.assertEqual(v3.g, 8)
        self.assertEqual(v3.b, 15)

        self.assertEqual(v.r, 1)
        self.assertEqual(v2.r, 3)

    def test_mul_scalar(self):
        v = Vec3(1, 2, 3)
        v2 = v * 2
        self.assertEqual(v2.r, 2)
        self.assertEqual(v2.g, 4)
        self.assertEqual(v2.b, 6)

        self.assertEqual(v.r, 1)

    def test_mul_vec(self):
        v = Vec3(1, 2, 3)
        v2 = Vec3(3, 4, 5)
        v3 = v * v2
        self.assertEqual(v3.r, 3)
        self.assertEqual(v3.g, 8)
        self.assertEqual(v3.b, 15)

        self.assertEqual(v.r, 1)
        self.assertEqual(v2.r, 3)

    def test_div_scalar(self):
        v = Vec3(10, 20, 30)
        v2 = v / 2
        self.assertEqual(v2.r, 5)
        self.assertEqual(v2.g, 10)
        self.assertEqual(v2.b, 15)

        self.assertEqual(v.r, 10)

    def test_div_vec(self):
        v2 = Vec3(5, 20, 24)
        v1 = Vec3(5, 4, 3)
        v2 /= v1
        self.assertEqual(v2.r, 1)
        self.assertEqual(v2.g, 5)
        self.assertEqual(v2.b, 8)

        self.assertEqual(v1.r, 5)
        self.assertEqual(v1.g, 4)

    def test_unit_vector(self):
        v = Vec3(5, 10, 20)
        u = v.unit_vector()
        self.assertEqual(u.r, 0.25)
        self.assertEqual(u.g, 0.50)
        self.assertEqual(u.b, 1.0)
