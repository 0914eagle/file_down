
MOD = 10**9 + 7

def count_ways(N, M, conditions):
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(4):
            for k in range(4):
                dp[i + 1][j][k] = dp[i][j][k]

        for l, r, x in conditions:
            for j in range(4):
                for k in range(4):
                    if j + (k == 1) + (k == 2) == x:
                        dp[i + 1][k][j] -= dp[r][j][k]
                        dp[i + 1][k][j] %= MOD
                    else:
                        dp[i + 1][k][j] = 0

    total_ways = sum(sum(dp[N][j][k] for j in range(4)) for k in range(4)) % MOD
    return total_ways

# Read input
N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
