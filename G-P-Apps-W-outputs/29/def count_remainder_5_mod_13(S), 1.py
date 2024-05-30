
def count_remainder_5_mod_13(S):
    MOD = 10**9 + 7
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1
    
    for i, c in enumerate(S):
        for j in range(13):
            if c == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
            else:
                dp[i+1][(j*10+int(c))%13] += dp[i][j]
        
        for j in range(13):
            dp[i+1][j] %= MOD
                
    return dp[-1][5]

# Input
S = input().strip()

# Output
print(count_remainder_5_mod_13(S))
```
