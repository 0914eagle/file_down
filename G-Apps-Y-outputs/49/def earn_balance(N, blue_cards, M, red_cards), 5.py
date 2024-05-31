
def earn_balance(N, blue_cards, M, red_cards):
    max_earnings = 0
    for card in blue_cards:
        earn_count = blue_cards.count(card) - red_cards.count(card)
        if earn_count > max_earnings:
            max_earnings = earn_count
    return max_earnings

# Read input
N = int(input())
blue_cards = [input().strip() for _ in range(N)]
M = int(input())
red_cards = [input().strip() for _ in range(M)]

# Calculate and print the maximum earnings
print(earn_balance(N, blue_cards, M, red_cards))
