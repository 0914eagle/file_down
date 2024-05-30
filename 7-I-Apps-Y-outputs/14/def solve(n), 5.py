
def solve(n):
    x = 1
    k = 2
    while n > 0:
        if n - x * k >= 0:
            n -= x * k
            x *= 2
            k += 1
        else:
            x = x * 2
            k -= 1
    return x

