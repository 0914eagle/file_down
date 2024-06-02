
def max_games_cv(n, games):
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1 - games[0]
    dp[0][1] = 1
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + 1 - games[i]
        dp[i][1] = dp[i-1][0] + games[i]
    return max(dp[-1])

# Input parsing
n = int(input())
games = list(map(int, input().split()))

# Call the function and print the result
print(max_games_cv(n, games))
