import matplotlib.pyplot as plt


def suite(x0, x1, n):
    if n == 0:
        return x0
    elif n == 1:
        return x1
    else:
        xnm1 = x0
        xn = x1
        for _ in range(0, n - 1):
            xnp1 = 111 - 1130 / xn + 3000 / (xn * xnm1)
            xnm1 = xn
            xn = xnp1
        return xn


def plot_suite(x0, x1, n):
    suite_xn = [x0, x1]
    if n == 0:
        return x0
    elif n == 1:
        return x1
    else:
        for i in range(1, n):
            xn = 111 - 1130 / suite_xn[i] + 3000 / (suite_xn[i] * suite_xn[i - 1])
            suite_xn += [xn]
        plt.plot(suite_xn)
        plt.savefig("suiteEx8.png")


if __name__ == '__main__':
    print(suite(11 / 2, 61 / 11, 0))
    print(suite(11 / 2, 61 / 11, 15))
    print(suite(11 / 2, 61 / 11, 16))
    print(suite(11 / 2, 61 / 11, 17))
    plot_suite(11 / 2, 61 / 11, 20000)
