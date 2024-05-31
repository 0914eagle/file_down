
def max_earnings(N, blue_cards, M, red_cards):
    earnings = 0
    blue_counts = {}
    red_counts = {}

    for card in blue_cards:
        if card in blue_counts:
            blue_counts[card] += 1
        else:
            blue_counts[card] = 1

    for card in red_cards:
        if card in red_counts:
            red_counts[card] += 1
        else:
            red_counts[card] = 1

    for key in blue_counts:
        if key in red_counts:
            earnings += blue_counts[key]

    return earnings

# Read input
N = int(input())
blue_cards = [input() for _ in range(N)]
M = int(input())
red_cards = [input() for _ in range(M)]

# Calculate and output result
result = max_earnings(N, blue_cards, M, red_cards)
print(result)
