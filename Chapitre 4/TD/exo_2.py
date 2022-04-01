import matplotlib.pyplot as plt


def euler(f, t, y0, n):
    dt = t / n
    t = [i * dt for i in range(n + 1)]
    y = [y0]
    for i in range(n):
        y.append(y[i] + dt * f(t[i], y[i]))
    return t, y


def f(t, y):
    return 3 * y - 3 * t


def fexact(t):
    return t + 1/3


if __name__ == "__main__":
    y0 = 1/3
    T = 20
    N = 100
    t, y = euler(f, T, y0, N)
    plt.plot(t, y, label="1/3")
    y0 = 0.333
    t, y = euler(f, T, y0, N)
    plt.plot(t, y, label="0.333")
    y = [fexact(i) for i in t]
    plt.plot(t, y, label="exact")
    plt.legend()
    plt.ylabel("y")
    plt.xlabel("t")
    plt.title("Euler diff 1/3 and 0.333")
    plt.savefig("exo2/f.png")
