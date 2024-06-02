
def count_ways(n, k, weights):
    dp = [[[0 for _ in range(2)] for _ in range(n+1)] for _ in range(k+1)]
    dp[0][0][0] = 1

    for i in range(1, k+1):
        for j in range(n+1):
            for p in range(2):
                dp[i][j][p] = dp[i][j][p] % 1000000007
                if j > 0 and i >= weights[j-1]:
                    dp[i][j][p] += dp[i-weights[j-1]][j-1][p]
                if j > 0 and i >= 2*weights[j-1]:
                    dp[i][j][p] += dp[i-2*weights[j-1]][j-1][1-p]
    
    min_rides = float('inf')
    total_ways = 0
    for i in range(1, k+1):
        rides = max(dp[i][n][0], dp[i][n][1])
        if rides < min_rides:
            min_rides = rides
            total_ways = (dp[i][n][0] + dp[i][n][1]) % 1000000007

    if min_rides == float('inf'):
        return -1, 0
    else:
        return min_rides, total_ways

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))

min_rides, total_ways = count_ways(n, k, weights)
print(min_rides)
print(total_ways)
