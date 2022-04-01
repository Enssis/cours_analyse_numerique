import math
import matplotlib.pyplot as plt


def euler(f, t, y0, n):
    dt = t / n
    t = [i * dt for i in range(n + 1)]
    y = [y0]
    for i in range(n):
        y.append(y[i] + dt * f(t[i], y[i]))
    return t, y


def erreur_euler(f, t, y0, n, fexact):
    dt = t / n
    t = [i * dt for i in range(n + 1)]
    y = [y0]
    for i in range(n):
        y.append(y[i] + dt * f(t[i], y[i]))
    return max([abs(y[i] - fexact(t[i])) for i in range(n + 1)])


def f1(t, y):
    return -y


def f2(t, y):
    return -y**2


def f1exact(t):
    return math.exp(-t)


def f2exact(t):
    return 1 / (1 + t)


if __name__ == "__main__":
    N = 1000
    T = 10
    t, y = euler(f1, T, 1, N)
    plt.ylabel("y")
    plt.xlabel("t")
    plt.plot(t, y, label="f1")
    y = [f1exact(i) for i in t]
    plt.plot(t, y, label="f1 exact")
    plt.legend()
    plt.title("Euler")
    plt.savefig("exo1/eulerf1.png")
    plt.clf()

    t, y = euler(f2, T, 1, N)
    plt.ylabel("y")
    plt.xlabel("t")
    plt.plot(t, y, label="f2")
    y = [f2exact(i) for i in t]
    plt.plot(t, y, label="f2 exact")
    plt.legend()
    plt.title("Euler")
    plt.savefig("exo1/eulerf2.png")
    plt.clf()

    err = [erreur_euler(f1, T, 1, 10 * 2 ** i, f1exact) for i in range(0, 8)]
    plt.ylabel("err")
    plt.xlabel("N")
    n = [10* 2 ** i for i in range(0, 8)]
    plt.plot(n, err, label="erreur f1")
    err = [erreur_euler(f1, T, 1, 10 * 2 ** i, f2exact) for i in range(0, 8)]
    plt.plot(n, err, label="erreur f2")
    plt.legend()
    plt.title("erreur Euler")
    plt.savefig("exo1/ereur_euler.png")