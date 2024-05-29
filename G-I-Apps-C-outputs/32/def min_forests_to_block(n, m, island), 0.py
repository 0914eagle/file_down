
def min_forests_to_block(n, m, island):
    dp = [[0] * m for _ in range(n)]
    for i in range(n-2, -1, -1):
        dp[i][m-1] = 1 if island[i][m-1] == "#" else dp[i+1][m-1]
    for j in range(m-2, -1, -1):
        dp[n-1][j] = 1 if island[n-1][j] == "#" else dp[n-1][j+1]

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            if island[i][j] == "#":
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0]

# Input
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Output
print(min_forests_to_block(n, m, island))
```
