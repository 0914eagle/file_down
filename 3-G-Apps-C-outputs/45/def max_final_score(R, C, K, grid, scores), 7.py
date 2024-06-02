
def max_final_score(R, C, K, grid, scores):
    dp = [[0] * C for _ in range(R)]
    
    for i in range(C):
        if grid[R-1][i] == '?':
            dp[R-1][i] = scores[i]
        else:
            dp[R-1][i] = 0
    
    for i in range(R-2, -1, -1):
        for j in range(C):
            if grid[i][j] == 'X':
                dp[i][j] = 0
            elif grid[i][j] == '.':
                dp[i][j] = dp[i+1][j]
            elif grid[i][j] == 'R':
                if j+1 < C:
                    dp[i][j] = dp[i+1][j+1]
            elif grid[i][j] == 'L':
                if j-1 >= 0:
                    dp[i][j] = dp[i+1][j-1]
            elif grid[i][j] == '?':
                if j+1 < C:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1])
                if j-1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1])
                dp[i][j] += scores[j]
    
    return max(dp[0])

# Input parsing
R, C, K = map(int, input().split())
grid = [input() for _ in range(R)]
scores = list(map(int, input().split()))

# Call the function and print the result
result = max_final_score(R, C, K, grid, scores)
print(result)
