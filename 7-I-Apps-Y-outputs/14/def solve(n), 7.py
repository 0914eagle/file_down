
def solve(n):
    x = 1
    k = 2
    while True:
        if n == x + 2*x + 4*x + 8*x + 16*x:
            return x
        x += 1
        k += 1

