
def max_calories(n, m, calories):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i-1][j], dp[i][j // 3] + calories[i-1]) if j <= m else dp[i-1][j]
    return dp[n][m]

# Read input
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Calculate and output the maximum number of calories Stan can consume
print(max_calories(n, m, calories))
