
MOD = 10**9 + 7

def count_special_numbers(n, k):
    dp = [[0] * (k + 1) for _ in range(2)]

    dp[0][0] = 1
    for i in range(1, n + 1):
        s = 0
        m = i
        while m:
            if m % 2:
                s += 1
            m //= 2

        for j in range(k + 1):
            for p in range(s, j + 1):
                dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][j - p]) % MOD

    res = 0
    for j in range(1, k + 1):
        res = (res + dp[n % 2][j]) % MOD

    return res

n = int(input(), 2)
k = int(input())
print(count_special_numbers(n, k))
```
