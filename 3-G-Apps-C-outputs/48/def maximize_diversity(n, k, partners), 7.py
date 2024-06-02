
def maximize_diversity(n, k, partners):
    partners.sort(key=lambda x: (x[2], x[3]), reverse=True)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)
            for l in range(i):
                if partners[i-1][0] > partners[l][0] and partners[i-1][1] > partners[l][1]:
                    dp[i][j] = max(dp[i][j], dp[l][j-1] + 1)
    
    return dp[n][k]

# Input parsing
n, k = map(int, input().split())
partners = []
for _ in range(n):
    g, p, ga, pa = map(int, input().split())
    partners.append((g, p, ga, pa))

# Call the function and output the result
result = maximize_diversity(n, k, partners)
print(result)
