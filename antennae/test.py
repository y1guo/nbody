import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(directory)
sys.path.append(parent_directory)
from leapfrog import NBodySystem

n = 2
m = [1, 0]
x = [[0] * 3 for _ in range(n)]
v = [[0] * 3 for _ in range(n)]
t = 0
dt = 0.01

x[1][0] = 1
v[1][1] = 1

nbody = NBodySystem(n, m, x, v, t)

for _ in range(630):
    nbody.leapfrog(dt)
    for i in range(n):
        print(
            "{:>8.2f}{:>4d}{:>8.2f}{:>8.4f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}".format(
                nbody.time, i, *nbody.position[i], *nbody.velocity[i]
            ),
        )
