
def count_remainder_5(S):
    MOD = 10**9 + 7
    dp = [[0] * 13 for _ in range(len(S) + 1)]
    dp[0][0] = 1

    for i in range(len(S)):
        for j in range(13):
            if S[i] == '?':
                for d in range(10):
                    dp[i + 1][(j * 10 + d) % 13] += dp[i][j]
            else:
                d = int(S[i])
                for j in range(13):
                    dp[i + 1][(j * 10 + d) % 13] += dp[i][j]
        for j in range(13):
            dp[i + 1][j] %= MOD

    return dp[-1][5]

S = input().strip()
print(count_remainder_5(S))
```
