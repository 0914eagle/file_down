
def count_ways(n, k, weights):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1]:
                dp[i][j] += dp[i - 1][j - weights[i - 1]]
            dp[i][j] %= 1000000007

    if dp[n][k] == 0:
        return -1, 0

    min_rides = dp[n][k]
    ways = 0
    for i in range(n):
        if weights[i] == 100:
            ways += dp[i][k]
            ways %= 1000000007

    return min_rides, ways

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))

min_rides, ways = count_ways(n, k, weights)
print(min_rides)
print(ways)
