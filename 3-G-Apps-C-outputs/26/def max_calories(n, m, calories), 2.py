
def max_calories(n, m, calories):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j])
            for k in range(1, min(j+1, m+1)):
                dp[i][j] = max(dp[i][j], dp[i-1][j-k] + calories[i-1] + dp[i-2][min(2*k, m)])
    
    return dp[n][m]

# Input parsing
n, m = map(int, input().split())
calories = list(map(int, input().split()))

result = max_calories(n, m, calories)
print(result)
