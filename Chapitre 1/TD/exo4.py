
if __name__ == "__main__":
    Ie0 = 0.0953101798
    Ien = Ie0
    for i in range(1, 51):
        Ien = -10 * Ien + 1 / i
    print("Î50 =", Ien)
    e0 = 4 * 10 ** (-12)
    e50 = e0 * 10 ** 50
    print("e50", e50)

    I60 = 1 / (10 * 61)
    In = I60
    for n in range(60, 50, -1):
        In = -(1 / 10) * (In - 1/n)
    print("I50 =", In)
