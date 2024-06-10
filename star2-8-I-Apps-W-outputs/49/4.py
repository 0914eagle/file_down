
n, k = map(int, input().split())
h = list(map(int, input().split()))
mod = 998244353

def power(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def calc(a, b):
    res = 0
    for i in range(a, b):
        res = res * k % mod
    return res

res = 0
for i in range(n):
    if h[i] == k:
        res = res + calc(i, n) % mod
    else:
        res = res + calc(i, n - 1) % mod
    res %= mod

res = res * power(k - 1, mod - 2) % mod
print(res)

