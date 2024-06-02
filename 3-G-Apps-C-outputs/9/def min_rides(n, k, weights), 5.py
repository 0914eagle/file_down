
def min_rides(n, k, weights):
    total_weight = sum(weights)
    if total_weight % k != 0:
        return -1, 0

    target_weight = total_weight // k
    dp = [[0] * (n + 1) for _ in range(target_weight + 1)]
    dp[0][0] = 1

    for w in weights:
        for i in range(target_weight, -1, -1):
            for j in range(n, 0, -1):
                if i - w // 50 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - w // 50][j - 1]) % 1000000007

    return 1, dp[target_weight][n]

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))

# Call the function and print the output
min_rides_count, ways_count = min_rides(n, k, weights)
print(min_rides_count)
print(ways_count)
