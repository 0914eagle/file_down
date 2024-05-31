
def min_card_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    
    for card in cards:
        rank, suit = card[:-1], card[-1]
        suits[suit].append(rank)

    moves = 0
    for suit in suits.values():
        if suit:
            sorted_suit = sorted(suit)
            if suit == sorted_suit or suit == sorted_suit[::-1]:
                continue
            else:
                moves += 1

    return moves

# Input
n = int(input())
cards = input().split()

# Output
print(min_card_moves(n, cards))
