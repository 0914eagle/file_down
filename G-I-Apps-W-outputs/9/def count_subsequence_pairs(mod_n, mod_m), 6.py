
MOD = 10**9 + 7

def count_subsequence_pairs(mod_n, mod_m):
    N = len(mod_n)
    M = len(mod_m)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if mod_n[i - 1] == mod_m[j - 1]:
                dp[i][j] = (2 * dp[i - 1][j - 1] + 1) % MOD
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) % MOD

    return dp[N][M]

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

print(count_subsequence_pairs(S, T))
```
