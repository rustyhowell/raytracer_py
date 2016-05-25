#!/usr/bin/env python
from random import random
from math import sqrt
from progressbar import ProgressBar, Percentage, ETA, Bar

from camera import Camera
from vector3 import Vec3, dot, unit_vector
from ray import Ray
from hitable import Sphere, HitableList, HitRecord

def random_in_unit_sphere():
    while True:
        p = Vec3(random(), random(), random()) * 2.0 - Vec3(1, 1, 1)
        if dot(p, p) < 1.0:
            return p


def color(ray_, world):
    assert isinstance(world, HitableList)
    hit, rec = world.hit(ray_, 0.0, 99999999999)
    if hit:
        target = rec.p + rec.normal + random_in_unit_sphere()
        return color(Ray(rec.p, target - rec.p), world) * 0.5
    else:
        unit_dir = unit_vector(ray_.direction)
        t = 0.5 * (unit_dir.y + 1.0)
        return Vec3(1, 1, 1) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t


if __name__ == '__main__':

    nx = 200
    ny = 100
    ns = 100

    lower_left = Vec3(-2, -1, -1)
    horizontal = Vec3(4, 0, 0)
    vertical = Vec3(0, 2, 0)
    origin = Vec3(0, 0, 0)
    world = HitableList()
    world.append(Sphere(Vec3(0, 0, -1), 0.5))
    world.append(Sphere(Vec3(0, -100.5, -1), 100))

    cam = Camera()
    pbar = ProgressBar(widgets=['Percentage ', Percentage(), ' ', ETA(),' ', Bar()], maxval=nx*ny).start()

    with open('image.ppm', 'w') as f:
        f.write('P3\n{} {}\n255\n'.format(nx, ny))
        for y, j in enumerate(xrange(ny-1, -1, -1)):
            for i in xrange(nx):
                col = Vec3(0, 0, 0)
                for _ in xrange(ns):
                    u = float(i + random()) / nx
                    v = float(j + random()) / ny

                    r = cam.get_ray(u, v)
                    p = r.point_at_parameter(2.0)
                    col += color(r, world)
                col /= float(ns)
                col = Vec3(sqrt(col.e0), sqrt(col.e1), sqrt(col.e2))
                ir = int(255.99 * col.r)
                ig = int(255.99 * col.g)
                ib = int(255.99 * col.b)
                f.write('{} {} {}\n'.format(ir, ig, ib))

                pbar.update(y * nx + i)
    pbar.finish()
    print("Done")
