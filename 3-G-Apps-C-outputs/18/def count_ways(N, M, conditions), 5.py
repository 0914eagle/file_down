
MOD = 10**9 + 7

def count_ways(N, M, conditions):
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(1, N + 1):
        for j in range(4):
            for k in range(4):
                dp[i][j][k] = dp[i - 1][j][k]
                if j > 0:
                    dp[i][j][k] += dp[i - 1][j - 1][k]
                if k > 0:
                    dp[i][j][k] += dp[i - 1][j][k - 1]
                dp[i][j][k] %= MOD

    total_ways = 0
    for l, r, x in conditions:
        ways = dp[r][x][3] - dp[l - 1][x][3]
        total_ways += ways
        total_ways %= MOD

    return total_ways

# Read input
N, M = map(int, input().split())
conditions = []
for _ in range(M):
    l, r, x = map(int, input().split())
    conditions.append((l, r, x))

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
