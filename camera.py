
from vector3 import Vec3
from ray import Ray

class Camera:
    def __init__(self):
        self.lower_left = Vec3(-2, -1, -1)
        self.horizontal = Vec3(4.0, 0, 0)
        self.vertical = Vec3(0, 2, 0)
        self.origin = Vec3(0, 0, 0)

    def get_ray(self, u, v):
        return Ray(self.origin,
                   self.lower_left + self.horizontal * u + self.vertical * v)
