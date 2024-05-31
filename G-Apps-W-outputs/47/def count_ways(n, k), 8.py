
def count_ways(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(1, k+1):
        dp[1][i] = 1
    
    for i in range(2, n+1):
        for j in range(1, k+1):
            for x in range(1, j+1):
                dp[i][j] = (dp[i][j] + dp[i-1][x]) % MOD
    
    total_ways = 0
    for i in range(1, k+1):
        total_ways = (total_ways + dp[n][i]) % MOD
    
    return total_ways

n, k = map(int, input().split())
print(count_ways(n, k))
