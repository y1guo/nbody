import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(directory)
sys.path.append(parent_directory)
from leapfrog import NBodySystem
import numpy as np

n = 2
m = np.full(n, 1.25).reshape((n, 1))
x = np.zeros((n, 3))
v = np.zeros((n, 3))
t = 0
dt = 0.01

x[0, 0] = -1.5
x[1, 0] = 1.5
v[0, 1] = -((1.25 / 12) ** 0.5)
v[1, 1] = (1.25 / 12) ** 0.5

nbody = NBodySystem(n, m, x, v, t)

for _ in range(1200):
    nbody.leapfrog(dt)
    for i in range(n):
        print(
            "{:>8.2f}{:>4d}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}".format(
                nbody.time, i, *nbody.position[i], *nbody.velocity[i]
            ),
        )
