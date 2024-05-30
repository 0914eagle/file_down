
MOD = 10**9 + 7

def count_remainder_5(s):
    dp = [[0] * 13 for _ in range(len(s) + 1)]
    dp[0][0] = 1

    for i in range(len(s)):
        for j in range(13):
            if s[i] == '?':
                for k in range(10):
                    dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
            else:
                dp[i + 1][(j * 10 + int(s[i])) % 13] += dp[i][j]
            dp[i + 1][j] %= MOD

    return dp[len(s)][5]

# Input
S = input().strip()

# Output
print(count_remainder_5(S))
```
