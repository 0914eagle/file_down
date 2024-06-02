
def min_rides(n, k, weights):
    total_weight = sum(weights)
    if total_weight % k != 0:
        return -1, 0

    dp = [[0] * (total_weight // k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(total_weight // k + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1] // k:
                dp[i][j] += dp[i - 1][j - weights[i - 1] // k]
            dp[i][j] %= 1000000007

    return dp[n][total_weight // k], dp[n][total_weight // k]

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function and print the output
result, ways = min_rides(n, k, weights)
print(result)
print(ways)
