
def count_ways(n, k):
    MOD = 10**9 + 7

    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = (dp[i-1][j] * (k-j+1) + dp[i][j-1]) % MOD
    
    return dp[n][n]

n, k = map(int, input().split())
print(count_ways(n, k))
