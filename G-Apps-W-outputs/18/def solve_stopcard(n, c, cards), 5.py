
import sys

def solve_stopcard(n, c, cards):
    cards.sort()
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(1, n - i + 1):
            probability = 1 / (n - i)
            dp[i][j] = max(probability * cards[i + j - 1] + (1 - probability) * dp[i + 1][j - 1],
                           cards[i] + dp[i + 1][j])
    
    return dp[0][c]

# Read input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Output the result
result = solve_stopcard(n, c, cards)
print("{:.6f}".format(result))
