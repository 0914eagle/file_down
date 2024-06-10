
from sys import stdin
from math import factorial

def nCk(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def solve(r, s, p):
    total = r + s + p
    r_prob = 0
    s_prob = 0
    p_prob = 0
    for i in range(1, r + 1):
        r_prob += nCk(r, i) * nCk(s + p, r + p - i) / nCk(total, r + s + p)
    for i in range(1, s + 1):
        s_prob += nCk(s, i) * nCk(r + p, s + p - i) / nCk(total, r + s + p)
    for i in range(1, p + 1):
        p_prob += nCk(p, i) * nCk(r + s, p + s - i) / nCk(total, r + s + p)
    return r_prob, s_prob, p_prob

r, s, p = map(int, stdin.readline().split())
print(*solve(r, s, p))

