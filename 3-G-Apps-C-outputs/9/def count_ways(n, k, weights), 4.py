
def count_ways(n, k, weights):
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            for l in range(2):
                dp[i][j][l] = dp[i - 1][j][l]
                if j >= weights[i - 1]:
                    dp[i][j][l] += dp[i - 1][j - weights[i - 1]][1 - l]
                dp[i][j][l] %= 1000000007

    min_rides = float('inf')
    total_ways = 0

    for j in range(k + 1):
        if dp[n][j][1] > 0:
            min_rides = min(min_rides, max(j, k - j))
            total_ways += dp[n][j][1]

    if min_rides == float('inf'):
        return -1, 0

    return min_rides, total_ways % 1000000007

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))
weights = [50 if w == 50 else 100 for w in weights]

min_rides, total_ways = count_ways(n, k, weights)
print(min_rides)
print(total_ways)
