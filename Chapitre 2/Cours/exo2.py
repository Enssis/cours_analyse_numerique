def dicho(f, a, b, n):
    c = (a + b) / 2
    for _ in range(0, n):
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return c


def f(x):
    return x ** 2 + 3 * x - 25


if __name__ == '__main__':
    print(dicho(f, 0, 100, 50))

