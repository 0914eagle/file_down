
def solve(n, p):
    x = 0
    for i in range(n):
        x += p[i] ** (i + 1)
    return x

