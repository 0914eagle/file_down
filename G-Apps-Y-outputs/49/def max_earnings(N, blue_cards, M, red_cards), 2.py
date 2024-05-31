
def max_earnings(N, blue_cards, M, red_cards):
    max_earnings = 0

    for card in blue_cards:
        max_earnings += 1 if card in red_cards else 0

    return max_earnings

# Read input
N = int(input())
blue_cards = [input().strip() for _ in range(N)]
M = int(input())
red_cards = [input().strip() for _ in range(M)]

# Calculate and print max earnings
print(max_earnings(N, blue_cards, M, red_cards))
