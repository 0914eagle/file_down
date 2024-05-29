
def max_frogs(n, d, frogs):
    frogs.sort(key=lambda x: (-x[0], x[2]))  # Sort frogs by leap capacity descending and height ascending
    escaped = 0
    pile_height = [0] * (n+1)
    dp = [[0] * (d+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, d+1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if j < frogs[i-1][2]:
                continue
            if j >= frogs[i-1][0] and pile_height[i-1] + frogs[i-1][1] <= frogs[i-1][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-frogs[i-1][0]] + 1)
                if dp[i][j] > dp[i][j-1]:
                    pile_height[i] = pile_height[i-1] + frogs[i-1][1]
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
    
    return dp[n][d]

# Read input
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Call the function
result = max_frogs(n, d, frogs)
print(result)
