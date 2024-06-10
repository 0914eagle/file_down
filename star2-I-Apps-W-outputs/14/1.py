
from sys import stdin
from math import factorial

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def solve(r, s, p):
    n = r + s + p
    p_r = 0
    p_s = 0
    p_p = 0
    for i in range(1, n):
        p_r += nCk(n - 1, i) * (r / n) * ((s + p) / (n - i)) ** i
        p_s += nCk(n - 1, i) * (s / n) * ((r + p) / (n - i)) ** i
        p_p += nCk(n - 1, i) * (p / n) * ((r + s) / (n - i)) ** i
    return p_r, p_s, p_p

r, s, p = map(int, stdin.readline().split())
p_r, p_s, p_p = solve(r, s, p)
print(p_r, p_s, p_p)

