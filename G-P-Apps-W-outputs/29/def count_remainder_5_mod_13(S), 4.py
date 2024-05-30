
def count_remainder_5_mod_13(S):
    MOD = 10**9 + 7
    n = len(S)
    
    dp = [[0] * 13 for i in range(n+1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    dp[i+1][(j*10 + k) % 13] += dp[i][j]
            else:
                k = int(S[i])
                dp[i+1][(j*10 + k) % 13] += dp[i][j]
                
        for j in range(13):
            dp[i+1][j] %= MOD

    return dp[n][5]

S = input().strip()
print(count_remainder_5_mod_13(S))
```
