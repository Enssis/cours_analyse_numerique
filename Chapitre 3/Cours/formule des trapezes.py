
#inte = I
def trapeze(a, b, n, f):
    inte = (f(a) + f(b)) * 0.5
    dx = (b - a) / n
    for i in range(1, n):
        inte += f(a + i*dx)
    inte *= dx
    return inte