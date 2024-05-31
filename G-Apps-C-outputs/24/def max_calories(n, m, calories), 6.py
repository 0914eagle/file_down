
def max_calories(n, m, calories):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i-1][j]
            for k in range(i, 0, -1):
                if j >= calories[k-1]:
                    dp[i][j] = max(dp[i][j], dp[i-k][j-calories[k-1]] + calories[k-1])
    
    return dp[n][m]

# Input parsing
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Call the function and output the result
result = max_calories(n, m, calories)
print(result)
