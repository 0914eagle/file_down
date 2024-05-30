
MOD = 100003

def count_ways(N, M, c):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j >= c[i - 1]:
                dp[i][j] = (dp[i][j] + dp[i][j - c[i - 1]]) % MOD

    total_ways = dp[N][M]
    X = total_ways // MOD
    Y = total_ways % MOD

    return X, Y

# Read input
N, M = map(int, input().split())
c = list(map(int, input().split()))

# Calculate and output the result
X, Y = count_ways(N, M, c)
print(X, Y)
```
