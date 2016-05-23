from collections import namedtuple
from vector3 import Vec3, dot
from math import sqrt
from ray import Ray

HitRecord = namedtuple("HitRecord", ['t', 'p', 'normal'])

class Hitable:

    def hit(self, ray_, t_min, t_max):
        """
        Determine if the ray will hit the object
        :param ray_:
        :param t_min:
        :param t_max:
        :return: Return a tuple:  true/hitrecord or False, None
        """
        raise NotImplemented("Override in subclass")


class Sphere(Hitable):

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, ray_, t_min, t_max):
        assert isinstance(ray_, Ray)
        oc = ray_.origin - self.center
        a = dot(ray_.direction, ray_.direction)
        b = dot(oc, ray_.direction)
        c = dot(oc, oc) - self.radius * self.radius
        discriminant = b * b - a * c

        if discriminant > 0.0:
            temp = (-b - sqrt(b*b - a * c)) / a
            if t_min < temp < t_max:
                p = ray_.point_at_parameter(temp)
                rec = HitRecord(t=temp,
                                p=p,
                                normal=(p - self.center) / self.radius
                                )

                return True, rec

            temp = (-b + sqrt(b*b - a * c)) / a
            if t_min < temp < t_max:
                p = ray_.point_at_parameter(temp)
                rec = HitRecord(t=temp,
                                p=p,
                                normal=(p - self.center) / self.radius
                                )
                return True, rec

        return False, None


class HitableList(Hitable):
    def __init__(self):
        self.shapes = []

    def append(self, shape):
        self.shapes.append(shape)

    def hit(self, ray_, t_min, t_max):
        hit_anything = False
        closest_so_far = t_max
        rec = None
        for shape in self.shapes:
            hit, tmprec = shape.hit(ray_, t_min, closest_so_far)
            if hit:
                hit_anything = True
                closest_so_far = tmprec.t
                rec = tmprec
        return hit_anything, rec
