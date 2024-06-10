
from collections import defaultdict
from math import gcd

MOD = 998244353

def inverse(x):
    return pow(x, MOD - 2, MOD)

def solve(n, m, d, a, b):
    d.sort()
    a.sort()
    
    damage = [0] * m
    for i in range(n):
        for j in range(m):
            if a[j] > 0 and d[i] < b[j]:
                continue
            damage[j] += 1
            a[j] -= 1
    
    for i in range(m):
        g = gcd(damage[i], n)
        damage[i] = damage[i] * inverse(n) % MOD
    
    return damage

