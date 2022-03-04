import math
import numpy as np


def dicho(f, a, b, e):
    c = (a + b) / 2
    n = math.floor(np.log((b - a) / e) / np.log(2))
    for _ in range(n + 1):
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return a, b, c


def f(x):
    return x ** 4 + x ** 3 - 1


if __name__ == '__main__':
    print(dicho(f, 0, 1, 0.1))

