
def find_min_depth(r, c, grid):
    dp = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        dp[i][0] = grid[i][0]

    for j in range(1, c):
        for i in range(r):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[max(0, i-1)][j-1], dp[min(r-1, i+1)][j-1])

    min_depth = min(dp[i][-1] for i in range(r))
    return min_depth

# Input processing
input_lines = input().split("\n")
r, c = map(int, input_lines[0].split())
grid = [list(map(int, line.split())) for line in input_lines[1:]]

# Call the function with input values
result = find_min_depth(r, c, grid)
print(result)
```
