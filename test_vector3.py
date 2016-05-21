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

    def test_squared_length(self):
        v = Vec3(1, 2, 3)
        self.assertEqual(v.squared_length(), 14.0)

    def test_mul_scalar(self):
        v = Vec3(1, 2, 3)
        v2 = v * 2
        self.assertEqual(v2.r, 2)
        self.assertEqual(v2.g, 4)
        self.assertEqual(v2.b, 6)

        self.assertEqual(v.r, 1)

    def test_mul_vecl(self):
        v = Vec3(1, 2, 3)
        v2 = Vec3(3, 4, 5)
        v3 = v * v2
        self.assertEqual(v3.r, 3)
        self.assertEqual(v3.g, 8)
        self.assertEqual(v3.b, 15)

        self.assertEqual(v.r, 1)
        self.assertEqual(v2.r, 3)
