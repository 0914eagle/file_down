
def solve(n, m):
    MOD = 10**9 + 7
    f = [1] * (m + 1)
    for i in range(1, m + 1):
        f[i] = f[i - 1] * i % MOD
    res = 0
    for i in range(1, m + 1):
        if m % i == 0:
            res = (res + f[n] * pow(f[n - 1], MOD - 2, MOD) * pow(f[i], MOD - 2, MOD) * pow(f[m // i], MOD - 2, MOD)) % MOD
    return res

n, m = map(int, input().split())
print(solve(n, m))

