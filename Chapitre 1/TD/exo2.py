import math


def calcul_racines(a, b, c):
    if b % 2 == 0:
        b = b / 2
        delta2 = b ** 2 - a * c
        if delta2 > 0:
            d2 = math.sqrt(delta2)
            x1 = (-b + d2) / a
            x2 = (-b - d2) / a
            correct_x2 = c / x1
            return x1, x2, correct_x2
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        d = math.sqrt(delta)
        x1 = (-b + d) / 2 * a
        x2 = (-b - d) / 2 * a
        return x1, x2


if __name__ == "__main__":
    print(calcul_racines(1, -1634, 2))
