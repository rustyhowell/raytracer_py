__author__ = 'rhowell'
from vector3 import Vec3, random_in_unit_sphere, reflect, unit_vector, dot
from ray import Ray

class Material:
    def scatter(self, ray_in, hit_record):
        """

        :param ray_in:
        :param hit_record:
        :return: Tuple of bool, Vec3 attenuation, Ray scattered
        """
        raise NotImplemented()


class Lambertian(Material):
    def __init__(self, albedo):
        assert isinstance(albedo, Vec3)
        self.albedo = albedo

    def scatter(self, ray_in, hit_record):
        target = hit_record.p + hit_record.normal + random_in_unit_sphere()
        scattered = Ray(hit_record.p, target - hit_record.p)
        return True, self.albedo, scattered


class Metal(Material):
    def __init__(self, albedo, fuzz):
        assert isinstance(albedo, Vec3)
        self.albedo = albedo
        self.fuzz = fuzz if fuzz < 1 else 1

    def scatter(self, ray_in, hit_record):
        reflected = reflect(unit_vector(ray_in.direction), hit_record.normal)
        scattered = Ray(hit_record.p, reflected + self.fuzz * random_in_unit_sphere())
        b = dot(scattered.direction, hit_record.normal) > 0.0

        return b, self.albedo, scattered
