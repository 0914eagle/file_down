
def min_rides(n, k, weights):
    total_weight = sum(weights)
    if total_weight % k != 0:
        return -1, 0

    target_weight = total_weight // k
    dp = [[[0, 0] for _ in range(n+1)] for _ in range(target_weight+1)]
    dp[0][0][0] = 1

    for i in range(1, n+1):
        for j in range(target_weight+1):
            for l in range(2):
                dp[j][i][l] = dp[j][i-1][l]
                if j >= weights[i-1] // k:
                    dp[j][i][l] += dp[j - weights[i-1] // k][i-1][1-l]
                dp[j][i][l] %= 1000000007

    return dp[target_weight][n][0], dp[target_weight][n][1]

n, k = map(int, input().split())
weights = list(map(int, input().split()))

min_rides_count, ways_count = min_rides(n, k, weights)
print(min_rides_count)
print(ways_count)
