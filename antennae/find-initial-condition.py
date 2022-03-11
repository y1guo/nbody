from cmath import sqrt
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(directory)
sys.path.append(parent_directory)
from leapfrog import NBodySystem
import math

n = 2
m = [1.25, 1.25]
x = [[0] * 3 for _ in range(n)]
v = [[0] * 3 for _ in range(n)]
t = 0
dt = -0.0001
nstep = 100

x[0][0] = 0.25
x[1][0] = -0.25
v[0][1] = math.sqrt(1.25 / 6) * 3
v[1][1] = -math.sqrt(1.25 / 6) * 3

nbody = NBodySystem(n, m, x, v, t)

px = [[] for _ in range(3)]

for _ in range(10000):
    nbody.leapfrog(dt)
    # if _ % nstep == 0:
    #     for i in range(n):
            # print(
            #     "{:>8.2f}{:>4d}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}".format(
            #         nbody.time, i, *nbody.position[i], *nbody.velocity[i]
            #     ),
            # )
    #         print(nbody.time, i, *nbody.position[i], *nbody.velocity[i])
    #         for j in range(3):
    #             px[j].append(nbody.position[i][j])

for i in range(n):
    print(nbody.time, i, *nbody.position[i], *nbody.velocity[i])

# import matplotlib.pyplot as plt
# plt.figure()
# plt.scatter(px[0], px[1], s=1)
# plt.xlim([-0.75, 0.75])
# plt.ylim([-0.75, 0.75])
# plt.show()
