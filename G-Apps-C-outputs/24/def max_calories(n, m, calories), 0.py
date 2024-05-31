
def max_calories(n, m, calories):
    dp = [[0 for _ in range(n + 1)] for _ in range(3)]
    
    for i in range(1, n + 1):
        for j in range(1, 3):
            dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1] + min(m, calories[i - 1]))
            m = (m * 2) // 3
        
    return dp[2][n]

# Input
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Output
print(max_calories(n, m, calories))
