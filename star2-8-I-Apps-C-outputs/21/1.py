
def get_num_ways(n, k, weights):
    num_ways = [[0] * (k + 1) for _ in range(n + 1)]
    num_ways[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            num_ways[i][j] = num_ways[i - 1][j]
            if j >= weights[i - 1]:
                num_ways[i][j] += num_ways[i - 1][j - weights[i - 1]]
    return num_ways[n][k]
def minimum_rides(n, k, weights):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1]:
                dp[i][j] += dp[i - 1][j - weights[i - 1]]
    if dp[n][k] == 0:
        return -1
    rides = 0
    remaining_weight = k
    for i in range(n - 1, -1, -1):
        if remaining_weight >= weights[i] and dp[i][remaining_weight - weights[i]] > 0:
            remaining_weight -= weights[i]
            rides += 1
    return rides

n, k = map(int, input().split())
weights = list(map(int, input().split()))
print(minimum_rides(n, k, weights))
print(get_num_ways(n, k, weights) % 1000000007)

