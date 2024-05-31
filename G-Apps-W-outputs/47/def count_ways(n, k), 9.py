
def count_ways(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for j in range(1, k + 1):
        dp[1][j] = 1
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j] * j + dp[i][j - 1]) % MOD
    return dp[n][k]

n, k = map(int, input().split())
print(count_ways(n, k))
