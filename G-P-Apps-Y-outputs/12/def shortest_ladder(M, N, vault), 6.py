
def shortest_ladder(M, N, vault):
    dp = [[float('inf') for _ in range(N)] for _ in range(M)]
    dp[0][0] = 0
    
    for i in range(M):
        for j in range(N):
            if i > 0:
                dp[i][j] = min(dp[i][j], max(dp[i-1][j], abs(vault[i][j] - vault[i-1][j])))
            if j > 0:
                dp[i][j] = min(dp[i][j], max(dp[i][j-1], abs(vault[i][j] - vault[i][j-1])))
    
    return dp[M-1][N-1]

# Read input
M, N = map(int, input().split())
vault = []
for _ in range(M):
    vault.append(list(map(int, input().split())))

# Call the function and output the result
print(shortest_ladder(M, N, vault))
```
