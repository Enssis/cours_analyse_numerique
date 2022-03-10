def pts_milieux(f, a, b, n):
    inte = 0
    dx = (b-a) / n
    for i in range(n):
        inte += f(a + i * dx + dx / 2)
    inte *= dx
    return inte

