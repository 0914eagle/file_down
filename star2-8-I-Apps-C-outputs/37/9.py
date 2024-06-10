
from sys import stdin

def solve():
    [d, b, f, t0, t1, t2] = list(map(int, stdin.readline().split()))
    if d == 1:
        return b + 100*f
    elif d == 2:
        return max(b + 100*f, b + 200*f)
    elif d == 3:
        return max(b + 100*f, b + 200*f, b + 200*f + 300*t0, b + 300*f, b + 300*f + 300*t0)
    else:
        return 0


print(solve())

