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

    def test_scalar_mul(self):
        v = Vec3(1, 2, 3)
        v2 = v * 2
        self.assertEqual(v2.r, 2)
        self.assertEqual(v2.g, 4)
        self.assertEqual(v2.b, 5)
        