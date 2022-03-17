def simpson(f, a, b, n):
    dx = (b - a) / n
    inte = f(a) + f(b) + 4*f(a + 0.5*dx)
    for i in range(1, n):
        inte += 2 * f(a + i*dx) + 4 *f(a + i*dx + 0.5 * dx)
    inte *= dx / 6
    return inte


def f(x):
    return x


if __name__ == '__main__':
    print(simpson(-1, 1, 4, f))