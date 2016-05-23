#!/usr/bin/env python
from vector3 import Vec3, dot
from ray import Ray

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = dot(r.direction, r.direction)
    b = 2.0 * dot(oc, r.direction)
    c = dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    return discriminant > 0.0


def color(ray_):
    if hit_sphere(Vec3(0, 0, -1), 0.5, ray_):
        return Vec3(1, 0, 0)
    unit_dir = ray_.direction.unit_vector()
    t = 0.5 * (unit_dir.y + 1.0)
    return Vec3(1, 1, 1) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t


if __name__ == '__main__':
    with open('image.ppm', 'w') as f:
        nx = 200
        ny = 100
        f.write('P3\n{} {}\n255\n'.format(nx, ny))

        lower_left = Vec3(-2, -1, -1)
        horizontal = Vec3(4, 0, 0)
        vertical = Vec3(0, 2, 0)
        origin = Vec3(0, 0, 0)
        for j in xrange(ny-1, -1, -1):
            for i in xrange(nx):
                u = float(i) / nx
                v = float(j) / ny

                r = Ray(origin, lower_left + horizontal * u + vertical * v)
                col = color(r)
                ir = int(255.99 * col.r)
                ig = int(255.99 * col.g)
                ib = int(255.99 * col.b)
                f.write('{} {} {}\n'.format(ir, ig, ib))
