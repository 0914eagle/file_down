
def sort_cards(hand):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}

    for card in hand:
        suits[card[1]].append(card)

    moves = 0
    for suit, cards in suits.items():
        if len(cards) > 1:
            sorted_cards = sorted(cards, key=lambda x: x[0])

            if cards != sorted_cards and cards != sorted_cards[::-1]:
                moves += 1

    return moves

# Input
n = int(input())
hand = input().split()

# Output
print(sort_cards(hand))
