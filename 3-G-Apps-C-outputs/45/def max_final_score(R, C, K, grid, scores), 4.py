
def max_final_score(R, C, K, grid, scores):
    dp = [[0] * C for _ in range(R)]
    
    for i in range(C):
        if grid[R-1][i] == '?':
            dp[R-1][i] = scores[i]
    
    for i in range(R-2, -1, -1):
        for j in range(C):
            if grid[i][j] == 'X':
                continue
            if grid[i][j] == '.':
                dp[i][j] = max(dp[i][j], dp[i+1][j])
            if grid[i][j] == '?':
                dp[i][j] = max(dp[i][j], dp[i+1][j] + scores[j])
            if j > 0 and grid[i][j-1] == 'R':
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            if j < C-1 and grid[i][j+1] == 'L':
                dp[i][j] = max(dp[i][j], dp[i][j+1])
    
    max_score = 0
    for i in range(C):
        max_score = max(max_score, dp[0][i])
    
    return max_score

# Input
R, C, K = map(int, input().split())
grid = [list(input()) for _ in range(R)]
scores = list(map(int, input().split()))

# Output
print(max_final_score(R, C, K, grid, scores))
