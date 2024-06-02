
MOD = 10**9 + 7

def count_ways(N, M, conditions):
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for i in range(1, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j + k + l <= 3:
                        dp[i][k][l] = (dp[i][k][l] + dp[i-1][j][k]) % MOD

    for l, r, x in conditions:
        new_dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
        for i in range(N+1):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j + k + l <= 3:
                            new_dp[i][k][l] = (new_dp[i][k][l] + dp[i][j][k]) % MOD
        dp = new_dp

        for i in range(r+1, N+1):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j + k + l <= 3:
                            dp[i][k][l] = (dp[i][k][l] - dp[r][j][k]) % MOD

    total_ways = sum(sum(dp[N][j][k] for j in range(4) for k in range(4)) for l in range(4)) % MOD
    return total_ways

# Read input
N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
