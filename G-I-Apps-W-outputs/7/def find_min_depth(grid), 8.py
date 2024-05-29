
def find_min_depth(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    for col in range(cols - 2, -1, -1):
        for row in range(rows):
            # Get current cell value
            cur_val = grid[row][col]

            # Get the minimum depth for the next column
            next_col_depth = float('inf')
            if row != 0:
                next_col_depth = min(next_col_depth, dp[row - 1][col + 1])
            if row != rows - 1:
                next_col_depth = min(next_col_depth, dp[row + 1][col + 1])
            next_col_depth = min(next_col_depth, dp[row][col + 1])

            dp[row][col] = max(cur_val, next_col_depth)

    return min(row[0] for row in dp)

# Input parsing
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output
print(find_min_depth(grid))
```
