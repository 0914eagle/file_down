
def confusion(n, k):
    MOD = 1000000007
    dp = [[0 for i in range(n)] for j in range(k + 1)]
    for i in range(1, n):
        dp[1][i] = 1
        for j in range(1, k):
            dp[j + 1][i] = dp[j + 1][i - 1]
            dp[j + 1][i] += (dp[j][i - 1] - dp[j][i - 2] + MOD)
            dp[j + 1][i] %= MOD
    return dp[k][n - 1]

n, k = map(int, input().split())
print(confusion(n, k))
