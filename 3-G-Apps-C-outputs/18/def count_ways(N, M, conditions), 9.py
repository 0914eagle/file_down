
MOD = 10**9 + 7

def count_ways(N, M, conditions):
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(1, N + 1):
        for j in range(4):
            for k in range(4):
                dp[i][j][k] = dp[i - 1][j][k]

        for l, r, x in conditions:
            for j in range(4 - x):
                for k in range(4):
                    dp[i][j + x][k | (1 << x)] += dp[l - 1][j][k]
                    dp[i][j + x][k | (1 << x)] %= MOD

    ans = 0
    for j in range(4):
        for k in range(4):
            if bin(k).count('1') == 3:
                ans += dp[N][j][k]
                ans %= MOD

    return ans

# Read input
N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
