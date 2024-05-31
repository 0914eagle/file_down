
def count_ways(n, k):
    MOD = 10**9 + 7

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

    total_ways = dp[n][k]
    return total_ways

# Read input values
n, k = map(int, input().split())

# Calculate and print the answer modulo (10^9 + 7)
result = count_ways(n, k)
print(result)
