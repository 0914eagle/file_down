
from math import factorial
def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
def solve(n, m, s1, s2):
    p, q = 1, 1
    for i in range(n):
        if s1[i] == 0:
            p *= m
            q *= ncr(m + n - i - 1, n - i - 1)
    return p // q
def main():
    n, m = map(int, input().split())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    p = solve(n, m, s1, s2)
    mod = 10**9 + 7
    q = pow(p, mod - 2, mod)
    r = (p * q) % mod
    print(r)
main()

