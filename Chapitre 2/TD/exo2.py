
def newton(x0, n, f, df):
    xn = x0
    for i in range(n):
        xn -= f(xn) / df(xn)
    return xn


def lagrange(x0, f, n, b):
    xn = x0
    fb = f(b)
    for i in range(n):
        xn = -fb * (b - xn) / (fb - f(xn)) + b
    return xn


def g(x):
    return (x/5) ** 5 + 5 * x ** 3 - 7 * x ** 2 + 1


def dg(x):
    return x**4 + 15 * x ** 2 - 14 * x


def sqrt2(x):
    return x ** 2 - 2


def dsqrt2(x):
    return 2 * x


if __name__ == "__main__":
    f = g
    df = dg
    a, b = 0.5, 2
    xl = a
    xn = b
    n = 5
    roll = 0
    precision = 10
    while int((10 ** precision) * xl) != int((10 ** precision) * xn):
        xl = lagrange(xl, f, n, b)
        xn = newton(xn, n, f, df)
        print(roll, ": \nlagrange :", xl, "\nnewton :", xn, "\n")
        roll += 1
    alpha = int((10 ** precision) * xl) / (10 ** precision)
    print("alpha :", alpha, ", f(alpha) :", g(alpha))
