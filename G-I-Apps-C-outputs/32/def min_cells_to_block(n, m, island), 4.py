
def min_cells_to_block(n, m, island):
    # Initialize a grid to keep track of minimum number of cells to block at each cell
    dp = [[float('inf')] * m for _ in range(n)]
    
    # Base case: starting cell
    dp[0][0] = 0 if island[0][0] == '.' else 1
    
    # Fill up the grid using dynamic programming
    for i in range(n):
        for j in range(m):
            if i < n-1:
                if island[i+1][j] == '.':
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j] + (1 if island[i][j] == '.' else 0))
            if j < m-1:
                if island[i][j+1] == '.':
                    dp[i][j+1] = min(dp[i][j+1], dp[i][j] + (1 if island[i][j] == '.' else 0))
    
    return dp[n-1][m-1]

# Input parsing
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Call the function and print the result
print(min_cells_to_block(n, m, island))
```
