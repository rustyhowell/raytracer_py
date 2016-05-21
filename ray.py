from vector3 import Vec3

class Ray:
    def __init__(self, a, b):
        assert isinstance(a, Vec3)
        assert isinstance(b, Vec3)
        self.A = a
        self.B = b

    @property
    def origin(self):
        return self.A

    @property
    def direction(self):
        return self.B

    def point_at_parameter(self, t):
        return self.A + t * self.B
