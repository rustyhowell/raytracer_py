#!/usr/bin/env python
from vector3 import Vec3

if __name__ == '__main__':
    with open('image.ppm', 'w') as f:
        nx = 200
        ny = 100
        f.write('P3\n{} {}\n255\n'.format(nx, ny))
        for j in xrange(ny-1, 0, -1):
            for i in xrange(nx):

                col = Vec3(float(i) / nx, float(j) / ny, 0.2)
                ir = int(255.99 * col.r)
                ig = int(255.99 * col.g)
                ib = int(255.99 * col.b)
                f.write('{} {} {}\n'.format(ir, ig, ib))
