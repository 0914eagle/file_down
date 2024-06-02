
def max_calories(n, m, calories):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            for k in range(1, j + 1):
                dp[i][j] = max(dp[i][j], min(calories[i-1], j) + dp[i-1][j - min(calories[i-1], j)] + dp[i-1][j - k])
    
    return dp[n][m]

# Input
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Output
print(max_calories(n, m, calories))