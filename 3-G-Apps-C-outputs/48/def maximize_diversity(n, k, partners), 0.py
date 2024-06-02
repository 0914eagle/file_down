
def maximize_diversity(n, k, partners):
    partners.sort(key=lambda x: (x[2], x[3]), reverse=True)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)
            if partners[i-1][2] != 0 and j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

    return dp[n][k]

# Input parsing
n, k = map(int, input().split())
partners = []
for _ in range(n):
    g, p, ga, pa = map(int, input().split())
    partners.append((g, p, ga, pa))

result = maximize_diversity(n, k, partners)
print(result)
