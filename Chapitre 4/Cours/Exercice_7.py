import numpy as np


def euler_pendule(T, N, theta0, thetap0, g, l):
    dt = T/N
    t = np.linspace(0, T, N+1)
    y1 = theta0 * np.ones(N+1)
    y2 = thetap0 * np.ones(N+1)
    for i in range(N):
        y1[i+1] = y1[i] + dt * y2[i]
        y2[i+1] = y2[i] - dt * (g / l) * np.sin(y1[i])
    return t, y1