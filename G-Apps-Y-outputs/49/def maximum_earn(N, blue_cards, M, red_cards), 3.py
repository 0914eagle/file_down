
def maximum_earn(N, blue_cards, M, red_cards):
    count = 0
    for card in blue_cards:
        count += 1 if card in red_cards else 0
    return count

# Input
N = int(input())
blue_cards = [input() for _ in range(N)]
M = int(input())
red_cards = [input() for _ in range(M)]

# Output
print(maximum_earn(N, blue_cards, M, red_cards))
