
def max_games(n, games):
    dp = [0] * n
    dp[0] = games[0]
    
    for i in range(1, n):
        if games[i] == 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    
    return dp[n-1]

# Input reading
n = int(input())
games = list(map(int, input().split()))

# Call the function and print the result
print(max_games(n, games))
