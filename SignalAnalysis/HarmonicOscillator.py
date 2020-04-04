# http://flothesof.github.io/harmonic-oscillator-three-methods-solution.html
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from scipy.integrate import odeint

sys.path.append(os.path.join("../"))
from src.base import plot2d


def deriv(u, t, omega_squared):
    "Provides derivative of vector u."
    xdot, x = u
    return [-omega_squared * x, xdot]


class HarmonicOdeSolver:
    def __init__(self, dt, x0, xd0, omega_squared):
        "Inits the solver."
        self.dt = dt
        self.dt_squared = dt**2
        self.t = dt
        self.omega_squared = omega_squared
        self.x0 = x0
        self.xd0 = xd0
        self.x = [xd0 * dt + x0, x0]

    def step(self):
        "Steps the solver."
        xt, xtm1 = self.x
        xtp1 = (2 - self.omega_squared * self.dt_squared) * xt - xtm1
        self.x = (xtp1, xt)
        self.t += self.dt

    def step_until(self, tmax, snapshot_dt):
        "Steps the solver until a given time, returns snapshots."
        ts = [self.t]
        vals = [self.x[0]]
        niter = max(1, int(snapshot_dt // self.dt))
        while self.t < tmax:
            for _ in range(niter):
                self.step()
            vals.append(self.x[0])
            ts.append(self.t)
        return np.array(ts), np.array(vals)


if __name__ == '__main__':
    solver = HarmonicOdeSolver(2e-1, 1, 0, 1)
    snapshot_dt = 0.3
    ts, vals = solver.step_until(12, snapshot_dt)

    #ts = np.arange(0, 12, snapshot_dt)
    y0 = [0, 1]
    scipysol0 = odeint(deriv, y0, ts, args=(1,))

    y1 = [1, 0]
    scipysol1 = odeint(deriv, y1, ts, args=(1,))

    obj = plot2d(aspect="auto")
    obj.axs.plot(ts, vals, label="val")
    obj.axs.plot(ts, scipysol0[:, 1], label="sol-0")
    obj.axs.plot(ts, scipysol1[:, 1], label="sol-1")
    obj.axs.legend()
    obj.SavePng()
