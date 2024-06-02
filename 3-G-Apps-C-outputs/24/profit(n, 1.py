profit(n, m, aggressiveness_levels, recruitment_costs, profitability_values):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[j][i] = max(dp[j][i], dp[j - 1][i - 1] + profitability_values[aggressiveness_levels[i - 1] - 1] - recruitment_costs[i - 1])
    
    return max(dp[m])

# Input parsing
n, m = map(int, input().split())
aggressiveness_levels = list(map(int, input().split()))
recruitment_costs = list(map(int, input().split()))
profitability_values = list(map(int, input().split()))

# Call the function and print the result
print(max_profit(n, m, aggressiveness_levels, recruitment_costs, profitability_values))
[/PYTHON