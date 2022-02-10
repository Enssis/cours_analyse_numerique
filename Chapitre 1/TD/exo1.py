def somme(n):
    s = 1
    for i in range(1, n + 1):
        s += 1/(i * (i + 1))
    return s


def somme_mieux(n):
    s = 0
    for i in range(n, 0, -1):
        s += 1 / (i * i + i)
    s += 1
    return s


if __name__ == "__main__":
    sM = 2 - 1/10000001
    sO = somme(10000000)
    print("Première somme : ")
    print("à la main :", str(sM))
    print("à l'ordi :", str(sO))
    print("erreur relative :", str(abs(sM - sO) / sM))

    sM = 2 - 1 / 10000001
    sO = somme_mieux(10000000)
    print("Seconde somme : ")
    print("à la main :", str(sM))
    print("à l'ordi :", str(sO))
    print("erreur relative :", str(abs(sM - sO) / sM))
