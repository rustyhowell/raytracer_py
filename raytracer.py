#!/usr/bin/env python
from vector3 import Vec3, dot, unit_vector
from ray import Ray
from hitable import Sphere, HitableList, HitRecord



def color(ray_, world):
    assert isinstance(world, HitableList)
    hit, rec = world.hit(ray_, 0.0, 99999999999)
    if hit:
        return Vec3(rec.normal.x + 1, rec.normal.y + 1, rec.normal.z + 1) * 0.5
    else:
        unit_dir = unit_vector(ray_.direction)
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
        world = HitableList()
        world.append(Sphere(Vec3(0, 0, -1), 0.5))
        world.append(Sphere(Vec3(0, -100.5, -1), 100))

        for j in xrange(ny-1, -1, -1):
            for i in xrange(nx):
                u = float(i) / nx
                v = float(j) / ny

                r = Ray(origin, lower_left + horizontal * u + vertical * v)
                p = r.point_at_parameter(2.0)
                col = color(r, world)
                ir = int(255.99 * col.r)
                ig = int(255.99 * col.g)
                ib = int(255.99 * col.b)
                f.write('{} {} {}\n'.format(ir, ig, ib))
