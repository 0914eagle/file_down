
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
                    if j + k == x:
                        dp[i][j][k] = 0

        for j in range(4):
            for k in range(4):
                if dp[i][j][k] == 0:
                    continue
                for c in range(1, 4):
                    if j + 1 <= 3:
                        dp[i][j + 1][c] += dp[i - 1][j][k]
                        dp[i][j + 1][c] %= MOD

    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD

    return ans

# Read input
N, M = map(int, input().split())
conditions = []
for _ in range(M):
    l, r, x = map(int, input().split())
    conditions.append((l, r, x))

# Calculate and print the result
result = count_ways(N, M, conditions)
print(result)
