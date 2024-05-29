
def min_cells_to_block_treasure(n, m, island):
    dp = [[0] * m for _ in range(n)]
    dp[n-1][m-1] = 1 if island[n-1][m-1] == "#" else 0

    for i in range(n-2, -1, -1):
        dp[i][m-1] = max(1, dp[i+1][m-1] - (island[i][m-1] == "#"))

    for j in range(m-2, -1, -1):
        dp[n-1][j] = max(1, dp[n-1][j+1] - (island[n-1][j] == "#"))

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - (island[i][j] == "#"))

    return dp[0][0]

# Input reading
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Call the function
result = min_cells_to_block_treasure(n, m, island)
print(result)
```
