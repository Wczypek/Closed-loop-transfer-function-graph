import numpy as np

t1 = 50
L = 2.5
H = 0.001
STEPS = int(t1 / H)


def integration(amp, a, b, k, m, u):

    y2p = []
    y1p = [0]
    y = [0]
    t = time_function()

    for i in range(STEPS - 1):
        y2p.append(-y1p[i] * a - y[i] * k * b * m + u[i] * k * b)
        y1p.append(y1p[i] + H / 1 * y2p[i])
        y.append(y[i] + H / 1 * y1p[i] + H * H / 2 * y2p[i])
    return y


def rectangular_func(amp, t):
    u = (amp * np.sign(np.sin(2 * np.pi * t / (t1 / L))) + 1) / 2
    return u


def sin_func(amp, t):
    u = amp * (np.sin(2 * np.pi * t / (t1 / L)))
    return u


def step_func(amp, t):
    u = [amp * x for x in range(len(t))]
    return u


def time_function():
    t = np.zeros(STEPS)
    for x in range(STEPS):
        t[x] = x * H
    return t
