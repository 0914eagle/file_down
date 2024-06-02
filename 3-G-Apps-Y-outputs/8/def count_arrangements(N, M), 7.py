
def count_arrangements(N, M):
    MOD = 10**9 + 7
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j] * j
            if j > 0:
                dp[i][j] += dp[i][j - 1] * i
            dp[i][j] %= MOD

    return dp[N][M]

N, M = map(int, input().split())
print(count_arrangements(N, M))
