
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
                    dp[i][j] += dp[i - w // 50][j - 1]
    
    return dp[target_weight][n], dp[target_weight][n] % 1000000007

# Input parsing
n, k = map(int, input().split())
weights = list(map(int, input().split()))

result, remainder = min_rides(n, k, weights)
print(result)
print(remainder)
