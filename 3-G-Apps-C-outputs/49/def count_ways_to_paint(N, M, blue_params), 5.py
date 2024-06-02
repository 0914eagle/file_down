
def count_ways_to_paint(N, M, blue_params):
    MOD = 100003

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j >= blue_params[i - 1]:
                dp[i][j] = (dp[i][j] + dp[i][j - blue_params[i - 1]]) % MOD

    total_ways = dp[N][M]
    X = total_ways // MOD
    Y = total_ways % MOD

    return X, Y

# Input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Output
X, Y_m = count_ways_to_paint(N, M, blue_params)
print(X, Y_m)