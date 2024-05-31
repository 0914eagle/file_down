
def expected_score(n, c, cards):
    cards.sort()
    
    dp = [[0.0] * (n + 1) for _ in range(c + 1)]
    
    for i in range(1, n + 1):
        dp[0][i] = dp[0][i - 1] + cards[i - 1]
    
    for i in range(1, c + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + cards[j - 1] / 2, dp[i][j - 1] + cards[j - 1])
    
    return dp[c][n]

# Input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print("{:.6f}".format(expected_score(n, c, cards)))
