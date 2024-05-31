
def max_balance_earned(N, S, M, T):
    max_balance = 0
    blue_cards = {}
    red_cards = {}

    for i in range(N):
        blue_cards[S[i]] = blue_cards.get(S[i], 0) + 1

    for i in range(M):
        red_cards[T[i]] = red_cards.get(T[i], 0) + 1

    for card in blue_cards:
        balance = blue_cards[card] - red_cards.get(card, 0)
        max_balance = max(max_balance, balance)

    return max_balance

# Read input
N = int(input())
S = [input().strip() for _ in range(N)]
M = int(input())
T = [input().strip() for _ in range(M)]

# Calculate and print max balance earned
print(max_balance_earned(N, S, M, T))
