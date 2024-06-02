
def max_final_score(R, C, K, grid, scores):
    dp = [[[0] * C for _ in range(2)] for _ in range(R + 1)]
    
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if grid[i][j] == 'X':
                continue
            for k in range(2):
                if grid[i][j] == '?' or grid[i][j] == 'L' and k == 0 or grid[i][j] == 'R' and k == 1:
                    dp[i][k][j] = max(dp[i][k][j], scores[j] + dp[i + 1][0][j - 1] if j > 0 else 0)
                    dp[i][k][j] = max(dp[i][k][j], scores[j] + dp[i + 1][1][j + 1] if j < C - 1 else 0)
                else:
                    dp[i][k][j] = max(dp[i][k][j], dp[i + 1][k][j])
    
    return max(dp[0][0] + dp[0][1])

# Read input
R, C, K = map(int, input().split())
grid = [input() for _ in range(R)]
scores = list(map(int, input().split()))

# Call the function and print the result
print(max_final_score(R, C, K, grid, scores))
