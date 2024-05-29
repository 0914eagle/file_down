
def min_forests_to_block(n, m, island):
    # Initialize a 2D list to keep track of the minimum number of forests to block at each cell
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]
    
    # Base case: Initialize starting cell and treasure cell to 0
    dp[0][0] = 0
    dp[n-1][m-1] = 0
    
    # Iterate through the island
    for i in range(n):
        for j in range(m):
            if island[i][j] == '.':
                # Check the cell to the left and above for minimum number of forests to block
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                
                # If the current cell has not been blocked, increment its value by 1
                dp[i][j] += 1 if island[i][j] == '.' else 0
    
    # The result is the minimum number of forests required to block the path to the treasure
    return dp[n-1][m-1]

# Read input
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Call the function and print the result
print(min_forests_to_block(n, m, island))
```
