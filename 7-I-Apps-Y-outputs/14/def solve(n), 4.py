
import math

def solve(n):
    x = 1
    k = 2
    while n > 0:
        n -= x
        x *= 2
        k += 1
    return x, k

t = int(input())
for _ in range(t):
    n = int(input())
    x, k = solve(n)
    print(x)

