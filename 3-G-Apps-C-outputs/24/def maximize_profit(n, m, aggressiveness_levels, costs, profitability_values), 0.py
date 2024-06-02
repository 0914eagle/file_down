
def maximize_profit(n, m, aggressiveness_levels, costs, profitability_values):
    dp = [[-float('inf')] * (n + m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(n + m + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= aggressiveness_levels[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - aggressiveness_levels[i - 1]] + profitability_values[aggressiveness_levels[i - 1]] - costs[i - 1])

    return max(dp[n])

# Input parsing
n, m = map(int, input().split())
aggressiveness_levels = list(map(int, input().split()))
costs = list(map(int, input().split()))
profitability_values = list(map(int, input().split()))

# Call the function and print the result
print(maximize_profit(n, m, aggressiveness_levels, costs, profitability_values))
