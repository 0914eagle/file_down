
from math import factorial

MOD = 998244353

def mod_inv(n, mod):
    return pow(n, mod - 2, mod)

def nCk(n, k, mod):
    return factorial(n, mod) * mod_inv(factorial(k, mod), mod) % mod * mod_inv(factorial(n - k, mod), mod) % mod

def solve(n):
    expected_value = 0
    for k in range(n + 1):
        expected_value += (n - k) * nCk(n, k, MOD)
    return expected_value // 2 % MOD

n = int(input())
print(solve(n))

