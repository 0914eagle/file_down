
def find_min_depth(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    dp = [[float('inf')] * cols for _ in range(rows)]
    
    # Fill the first column of dp with the depths of mud in the leftmost column of the grid
    for i in range(rows):
        dp[i][0] = grid[i][0]
    
    for j in range(1, cols):
        for i in range(rows):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], 
                                        dp[max(i-1, 0)][j-1], 
                                        dp[min(i+1, rows-1)][j-1])
    
    # Find the minimum depth in the rightmost column of dp to get the final result
    min_depth = min(dp[i][-1] for i in range(rows))
    
    return min_depth

# Parse input
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Call the function with the input grid
result = find_min_depth(grid)
print(result)
```
