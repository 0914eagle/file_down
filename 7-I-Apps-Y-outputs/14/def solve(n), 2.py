
def solve(n):
    x = 1
    k = 2
    while n > 0:
        n -= 2**(k-1) * x
        x += 1
        k += 1
    return x

