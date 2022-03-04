from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import math


def p(x):
    return x**3 + 2 * x ** 2 + 10 * x - 20


def phi(x):
    return 20 / (x ** 2 + 2 * x + 10)


def dichotomie(f, n, a, b):
    for i in range(n):
        c = (a + b)/2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def suite(f, x0, n):
    x = x0
    val = [x]
    for i in range(n):
        x = f(x)
        val.append(x)
    return x, val


if __name__ == '__main__':
    n = 54
    dicho = dichotomie(p, n, 1, 2)
    s, x = suite(phi, 1, n)
    print("Dichotomie :", dicho)
    print("Suite :", s)
    #print("(alpha - xn) / (alpha - xn-1)  :", [-(s - x[i + 1])/(s - x[i]) for i in range(n-1)])

    plt.plot()
    print("dif :", (dicho - s))
    print("fsolve : ", fsolve(p, 1)[0])

