import math
import matplotlib.pyplot as plt


def pts_milieux(f, a, b, n):
    inte = 0
    dx = (b-a) / n
    for i in range(n):
        inte += f(a + i * dx + dx / 2)
    inte *= dx
    return inte


def trapeze(f, a, b, n):
    inte = (f(a) + f(b)) * 0.5
    dx = (b - a) / n
    for i in range(1, n):
        inte += f(a + i*dx)
    inte *= dx
    return inte


def simpson(f, a, b, n):
    dx = (b - a) / n
    inte = f(a) + f(b) + 4*f(a + 0.5*dx)
    for i in range(1, n):
        inte += 2 * f(a + i*dx) + 4 *f(a + i*dx + 0.5 * dx)
    inte *= dx / 6
    return inte


def f(x):
    return math.exp(x)


if __name__ == '__main__':
    a, b = 0, 1
    iExact = math.exp(1) - 1
    size = 200
    pts_milieux_res = [pts_milieux(f, a, b, n) for n in range(1, size)]
    trapeze_res = [trapeze(f, a, b, n) for n in range(1, size)]
    simpson_res = [simpson(f, a, b, n) for n in range(1, size)]

    pts_milieux_en = [abs(iExact - pts_milieux_res[i]) for i in range(size - 1)]
    trapeze_en = [abs(iExact - trapeze_res[i]) for i in range(size - 1)]
    simpson_en = [abs(iExact - simpson_res[i]) for i in range(size - 1)]

    for n in range(size - 1):
        print("\n ---------- n =", n, "----------")
        print("pt milieux :", pts_milieux_en[n], pts_milieux_res[n])
        print("trapeze :", trapeze_en[n], trapeze_res[n])
        print("simpson :", simpson_en[n], simpson_res[n])

    x = [math.log(n) for n in range(1, size)]
    y_pts_millieux = [math.log(pts_milieux_en[n]) for n in range(size - 1)]
    y_trapeze = [math.log(trapeze_en[n]) for n in range(size - 1)]
    y_simpson = [math.log(simpson_en[n]) for n in range(size - 1)]

    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x, y_pts_millieux, label='pts_milieux')
    plt.plot(x, y_trapeze, label='trapeze')
    plt.plot(x, y_simpson, label='simpson')

    plt.legend()
    plt.savefig("exo1_methodes.png")
