
MOD = 10**9 + 7

def count_pairs(N, M, S, T):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = dp[i][j + 1]
            if S[i] == T[j]:
                dp[i + 1][j + 1] += dp[i][j] + 1
            dp[i + 1][j + 1] %= MOD
    
    total_pairs = 0
    for row in dp:
        total_pairs += sum(row)
        total_pairs %= MOD
    
    return total_pairs

# Input parsing
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# Output
print(count_pairs(N, M, S, T))
```
