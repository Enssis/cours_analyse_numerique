def simpson(vals, dx):
    n = len(vals)
    inte = vals[0] + vals[n - 1] + 4 * vals[1]
    for i in range(1, n, 2):
        inte += 2 * vals[i] + 4 * vals[i + 1]
    inte *= dx / 6
    return inte


def trapeze(vals, dx):
    n = len(vals)
    inte = (vals[0] + vals[n-1]) * 0.5
    for i in range(1, n):
        inte += vals[i]
    inte *= dx
    return inte


if __name__ == '__main__':
    acc = [30, 31.63, 33.44, 35.47, 37.75, 40.33, 43.29, 46.70, 50.67]
    print(simpson(acc, 10))
    print(trapeze(acc, 10))
