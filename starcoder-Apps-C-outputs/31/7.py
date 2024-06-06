
from fractions import Fraction
from functools import lru_cache

def solve(i, p):
    if i == n:
        return 0 if p >= P else float("inf")
    no = solve(i + 1, p)
    yes = e[i] + solve(i + 1, p * p[i])
    return min(no, yes)

if __name__ == "__main__":
    n, P = map(float, input().split())
    P = Fraction(P)
    p, e = [map(Fraction, input().split()) for _ in range(int(n))]
    print(solve(0, 1))
