
def max_games_in_cv(n, games):
    dp = [0] * n
    dp[0] = games[0]
    
    for i in range(1, n):
        if games[i] == 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    
    return dp[n-1]

# Input processing
n = int(input())
games = list(map(int, input().split()))

# Call the function and print the result
print(max_games_in_cv(n, games))
