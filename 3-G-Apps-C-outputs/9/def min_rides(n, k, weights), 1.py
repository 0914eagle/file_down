
def min_rides(n, k, weights):
    total_weight = sum(weights)
    if total_weight % k != 0:
        return -1, 0
    
    target_weight = total_weight // k
    dp = [[[0 for _ in range(target_weight + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(n + 1):
            for w in range(target_weight + 1):
                dp[i][j][w] = dp[i - 1][j][w]
                if j > 0 and w >= weights[i - 1]:
                    dp[i][j][w] += dp[i - 1][j - 1][w - weights[i - 1]]
    
    return dp[n][n][target_weight], dp[n][n][target_weight] % 1000000007

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))

result, remainder = min_rides(n, k, weights)
print(result)
print(remainder)
