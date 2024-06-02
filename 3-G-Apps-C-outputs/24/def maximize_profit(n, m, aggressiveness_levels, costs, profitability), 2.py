
def maximize_profit(n, m, aggressiveness_levels, costs, profitability):
    dp = [[-float('inf')] * (n + 1) for _ in range(n + m + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, n + m + 1):
            dp[i][j] = max(dp[i][j], dp[i][j - 1])
            if aggressiveness_levels[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - aggressiveness_levels[i - 1]] + profitability[aggressiveness_levels[i - 1] - 1] - costs[i - 1])

    return max(dp[n])

# Input parsing
n, m = map(int, input().split())
aggressiveness_levels = list(map(int, input().split()))
costs = list(map(int, input().split()))
profitability = list(map(int, input().split()))

# Call the function and print the result
print(maximize_profit(n, m, aggressiveness_levels, costs, profitability))
