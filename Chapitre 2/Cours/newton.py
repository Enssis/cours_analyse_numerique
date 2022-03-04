
def Newt(x0, n, f, df):
    xn = x0
    for i in range(n):
        xn -= f(xn) / df(xn)
    return xn


if __name__ == '__main__':
    print("hello")