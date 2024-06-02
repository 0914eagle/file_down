
MOD = 10**9 + 7

def count_ways(N, M, conditions):
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(1, N + 1):
        for j in range(4):
            for k in range(4):
                dp[i][j][k] = dp[i - 1][j][k]

        for l, r, x in conditions:
            for j in range(4):
                for k in range(4):
                    if j + (x == 1) + (k == 1) == 1:
                        dp[i][j][k] = 0

        for j in range(4):
            for k in range(4):
                if dp[i][j][k] == 0:
                    continue
                for c in range(1, 4):
                    if j + (c == 1) <= 3:
                        dp[i][j + (c == 1)][c] = (dp[i][j + (c == 1)][c] + dp[i][j][k]) % MOD

    total_ways = sum(sum(dp[N][j][k] for k in range(4)) for j in range(4)) % MOD
    return total_ways

# Read input
N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
