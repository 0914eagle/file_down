
def max_profit(n, m, aggressiveness, costs, profitability):
    dp = [[0] * (n + 1) for _ in range(n + m + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + m + 1):
            dp[j][i] = max(dp[j][i], dp[j - 1][i])
            if j >= aggressiveness[i - 1]:
                dp[j][i] = max(dp[j][i], dp[j - aggressiveness[i - 1]][i - 1] + profitability[aggressiveness[i - 1] - 1] - costs[i - 1])
    
    return max(dp[j][n] for j in range(n + m + 1))

# Input parsing
n, m = map(int, input().split())
aggressiveness = list(map(int, input().split()))
costs = list(map(int, input().split()))
profitability = list(map(int, input().split()))

# Call the function and print the result
print(max_profit(n, m, aggressiveness, costs, profitability))
