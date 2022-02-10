import math
import matplotlib.pyplot as plt


def expm10_taylor(n):
    res = 0
    for i in range(0, n + 1):
        res += ((-1) ** i) * (10 ** i) / math.factorial(i)
    return res


def exp10_taylor(n):
    res = 0
    for i in range(0, n + 1):
        res += (10 ** i) / math.factorial(i)
    return res


if __name__ == "__main__":
    em10 = math.exp(-10)
    print("Valeur de exp(-10) :", str(em10))
    emO = expm10_taylor(5000)
    print("premiere version : ", str(emO))
    print("erreur relative :", str(abs(em10 - emO) / em10))
    emO = 1 / exp10_taylor(5000)
    print("premiesecondere version : ", str(emO))
    print("erreur relative :", str(abs(em10 - emO) / em10))

    un = [(10 ** k) / math.factorial(k) for k in range(0, 200)]
    plt.plot(un)
    plt.savefig("exo3Un.png")
