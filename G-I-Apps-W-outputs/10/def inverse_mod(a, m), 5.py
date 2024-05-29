
MOD = 998244353

def inverse_mod(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def solve():
    n = int(input())
    treasure_values = list(map(int, input().split()))

    treasure_values.sort(reverse=True)
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + treasure_values[i]

    result = [0] * n
    for k in range(1, n+1):
        numerator = prefix_sum[-1] - prefix_sum[k]
        denominator = n - k + 1
        result[k-1] = (numerator * inverse_mod(denominator, MOD)) % MOD

    print(*result)

solve()
```
