
def min_depth_mud(r, c, grid):
    dp = [[0] * c for _ in range(r)]

    # Initialize the DP table with the first column
    for i in range(r):
        dp[i][0] = grid[i][0]

    # Evaluate the DP table
    for j in range(1, c):
        for i in range(r):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j] if i - 1 >= 0 else float('inf'), dp[i+1][j] if i + 1 < r else float('inf'))

    # Find the minimum depth in the last column
    min_depth = min(dp[i][c-1] for i in range(r))
    return min_depth

# Parse input
inp = input().strip().split()
r, c = int(inp[0]), int(inp[1])
grid = []
for _ in range(r):
    row = list(map(int, input().strip().split()))
    grid.append(row)

# Call the function and output the result
result = min_depth_mud(r, c, grid)
print(result)
```
