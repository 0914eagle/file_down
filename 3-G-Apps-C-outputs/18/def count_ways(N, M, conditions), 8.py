
MOD = 10**9 + 7

def count_ways(N, M, conditions):
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(1, N + 1):
        for j in range(4):
            for k in range(4):
                dp[i][j][k] = dp[i - 1][j][k]

        for l, r, x in conditions:
            for j in range(3, -1, -1):
                for k in range(3, -1, -1):
                    if j + k == x:
                        dp[i][j][k] = (dp[i][j][k] + dp[l - 1][j][k]) % MOD

    total_ways = 0
    for j in range(4):
        for k in range(4):
            total_ways = (total_ways + dp[N][j][k]) % MOD

    return total_ways

# Read input
N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
