import numpy as np

n = 2 # number of objects
x = np.zeros((n, 3))
v = np.zeros((n, 3))
nstep = 100000 # total number of steps
t = 0
dt = 0.01 # time step

def accel(x: np.ndarray) -> None:
    r = (x[0]**2 + x[1]**2 + x[2]**2)**0.5
    return - G * 1.0 * x / r**3

# start leapfrogging
for i in range(nstep):
    if (i % nout == 0):
        printstate(x, v, t, n)
    # evolve v by a half step
    v += accel(x) * dt / 2
    # evolve x by a full step
    x += v * dt
    # evolve v by a half step
    v += accel(x) * dt / 2
    t += dt
if (nstep % nout == 0):
    printstate(x, v, t, n)

