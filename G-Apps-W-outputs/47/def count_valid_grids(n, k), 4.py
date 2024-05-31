
MOD = 10**9 + 7

def count_valid_grids(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    return dp[n][k]

n, k = map(int, input().split())
result = count_valid_grids(n, k)
print(result)
