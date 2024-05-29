
def count_same_content_subsequences(N, M, S, T):
    MOD = 10**9 + 7
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(N+1):
        for j in range(M+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif S[i-1] == T[j-1]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] + 1) % MOD
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD
    
    return dp[N][M]

# Reading input
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# Print the result
print(count_same_content_subsequences(N, M, S, T))
```
