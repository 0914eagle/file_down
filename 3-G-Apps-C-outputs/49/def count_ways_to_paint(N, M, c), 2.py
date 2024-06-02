
def count_ways_to_paint(N, M, c):
    MOD = 100003
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            if j >= c[i - 1]:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
            else:
                dp[i][j] = dp[i - 1][j]

    total_ways = dp[N][M]
    X = total_ways // MOD
    Y = total_ways % MOD

    return X, Y

# Input
N, M = map(int, input().split())
c = list(map(int, input().split()))

# Output
X, Y = count_ways_to_paint(N, M, c)
print(X, Y)
