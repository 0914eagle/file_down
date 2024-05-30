
def count_remainder_5_mod_13(S):
    MOD = 10**9 + 7
    dp = [[0] * 13 for _ in range(len(S))]
    
    if S[0] == '?':
        for i in range(10):
            dp[0][i] = 1
    else:
        dp[0][int(S[0])] = 1
        
    for i in range(1, len(S)):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i][(k * 10 + j) % 13] += dp[i-1][k]
        else:
            for k in range(13):
                dp[i][(k * 10 + int(S[i])) % 13] += dp[i-1][k]
        
        for j in range(13):
            dp[i][j] %= MOD

    return dp[-1][5]

S = input().strip()
print(count_remainder_5_mod_13(S))
```
