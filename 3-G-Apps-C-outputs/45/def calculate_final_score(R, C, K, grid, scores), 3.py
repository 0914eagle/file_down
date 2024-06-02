
def calculate_final_score(R, C, K, grid, scores):
    dp = [[[0] * C for _ in range(R)] for _ in range(K)]
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'R':
                dp[0][i][j] = j
            elif grid[i][j] == 'L':
                dp[0][i][j] = -j
    
    for k in range(1, K):
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'X':
                    continue
                if j > 0 and grid[i][j-1] != 'X':
                    dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j-1])
                if j < C-1 and grid[i][j+1] != 'X':
                    dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j+1])
    
    max_score = 0
    for j in range(C):
        score = 0
        for k in range(K):
            score += scores[j]
            score += dp[k][R-1][j]
            max_score = max(max_score, score)
    
    return max_score

# Input parsing
R, C, K = map(int, input().split())
grid = [input() for _ in range(R)]
scores = list(map(int, input().split()))

# Calculate and output the maximum final score
print(calculate_final_score(R, C, K, grid, scores))
