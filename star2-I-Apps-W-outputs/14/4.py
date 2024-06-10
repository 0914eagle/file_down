
import sys

def solve(r, s, p):
    total = r + s + p
    r, s, p = r / total, s / total, p / total
    while True:
        new_r = p
        new_s = r
        new_p = s
        if abs(new_r - r) < 1e-9 and abs(new_s - s) < 1e-9 and abs(new_p - p) < 1e-9:
            break
        r, s, p = new_r, new_s, new_p
    return r, s, p

r, s, p = map(int, sys.stdin.read().split())
print(*solve(r, s, p))

