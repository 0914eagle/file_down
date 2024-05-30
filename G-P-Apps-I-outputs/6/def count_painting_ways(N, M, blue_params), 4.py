
def count_painting_ways(N, M, blue_params):
    MOD = 100003
    
    dp = [[[0 for _ in range(M+1)] for _ in range(M+1)] for _ in range(N+1)]
    
    for i in range(M+1):
        dp[1][i][i] = 1
    
    for i in range(2, N+1):
        for j in range(M+1):
            for k in range(j+1):
                for a in range(j+1):
                    dp[i][j][a] += dp[i-1][j][k]
                    dp[i][j][a] %= MOD
    
    total_ways = dp[N][M][blue_params[0]]
    
    return total_ways // MOD, total_ways % MOD

# Input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Output
X, Y = count_painting_ways(N, M, blue_params)
print(X, Y)
```
