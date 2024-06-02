
def max_final_score(R, C, K, grid, scores):
    dp = [[0] * C for _ in range(R)]
    
    for i in range(C):
        dp[0][i] = scores[i]
    
    for i in range(1, R):
        for j in range(C):
            if grid[i][j] == 'X':
                dp[i][j] = 0
            elif grid[i][j] == '.':
                dp[i][j] = dp[i-1][j]
            elif grid[i][j] == 'R':
                dp[i][j] = dp[i-1][min(j+1, C-1)]
            elif grid[i][j] == 'L':
                dp[i][j] = dp[i-1][max(j-1, 0)]
            elif grid[i][j] == '?':
                dp[i][j] = max(dp[i-1][max(j-1, 0)], dp[i-1][min(j+1, C-1)])
    
    return max(dp[-1])

# Input parsing
R, C, K = map(int, input().split())
grid = [input() for _ in range(R)]
scores = list(map(int, input().split()))

# Call the function and output the result
print(max_final_score(R, C, K, grid, scores))
