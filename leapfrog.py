from typing import List
import math


class NBodySystem:
    def __init__(
        self,
        n: int,
        m: List[float],
        x: List[List[float]],
        v: List[List[float]],
        t: float,
    ) -> None:
        assert len(m) == n
        for _ in [x, v]:
            assert len(_) == n
            for i in range(n):
                assert len(_[i]) == 3
        self.nbody = n
        self.mass = m
        self.position = x
        self.velocity = v
        self.time = t

    def leapfrog(self, dt: float) -> None:
        def accel(m: List[float], x: List[List[float]]) -> List[List[float]]:
            n = len(m)
            a = [[0] * 3 for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    dx = [x[i][_] - x[j][_] for _ in range(3)]
                    r = math.sqrt(dx[0] * dx[0] + dx[1] * dx[1] + dx[2] * dx[2])
                    for _ in range(3):
                        a[i][_] += -m[j] * dx[_] / r ** 3
                        a[j][_] += m[i] * dx[_] / r ** 3
            return a

        n = self.nbody
        a = accel(self.mass, self.position)
        for i in range(n):
            for _ in range(3):
                self.velocity[i][_] += a[i][_] * dt / 2  # half step v
        for i in range(n):
            for _ in range(3):
                self.position[i][_] += self.velocity[i][_] * dt  # full step x
        for i in range(n):
            for _ in range(3):
                self.velocity[i][_] += a[i][_] * dt / 2  # half step v
        self.time += dt
