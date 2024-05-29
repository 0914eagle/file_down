
def min_forests_to_block(n, m, island):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                dp[i][j] = 0
            elif island[i][j] == '#':
                dp[i][j] = float('inf')
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])
                if dp[i][j] == float('inf'):
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i][j], 1)
    
    return dp[0][0]

# Taking input
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Call the function and print the output
print(min_forests_to_block(n, m, island))
```
