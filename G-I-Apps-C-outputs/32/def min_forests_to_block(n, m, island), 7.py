
def min_forests_to_block(n, m, island):
    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(m):
            if island[i][j] == '#':
                continue
            if i + 1 < n:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j + 1 < m:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j])
    
    return dp[n-1][m-1]

# Read input
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Output result
print(min_forests_to_block(n, m, island))
```
