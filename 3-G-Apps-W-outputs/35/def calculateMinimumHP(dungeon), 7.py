
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[m][n - 1] = dp[m - 1][n] = 1
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            min_hp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(1, min_hp)
    
    return dp[0][0]

# Example dungeon
dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

print(calculateMinimumHP(dungeon))  # Output: 7
