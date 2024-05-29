
def find_min_mud_depth(r, c, grid):
    # Initialize dp array to store minimum mud depth for each cell
    dp = [[0] * c for _ in range(r)]
    
    # Copy first column of mud depths to dp array
    for i in range(r):
        dp[i][0] = grid[i][0]
    
    # Update dp array with minimum mud depth for each cell
    for j in range(1, c):
        for i in range(r):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[max(i-1, 0)][j-1], dp[min(i+1, r-1)][j-1])
    
    # Find the maximum mud depth Liam encounters on his route
    max_mud_depth = max(dp[i][-1] for i in range(r))
    
    return max_mud_depth

# Sample Input 1
grid1 = [
    [2, 1, 0, 8],
    [3, 7, 3, 5],
    [3, 1, 2, 4],
    [9, 0, 4, 6],
    [5, 3, 2, 3]
]
print(find_min_mud_depth(5, 4, grid1))  # Output: 3

# Sample Input 2
grid2 = [
    [3, 0],
    [1, 2]
]
print(find_min_mud_depth(2, 2, grid2))  # Output: 2
```
