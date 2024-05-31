
def min_card_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}

    for card in cards:
        rank, suit = card[:-1], card[-1]
        if rank == 'T':
            rank = 10
        elif rank == 'J':
            rank = 11
        elif rank == 'Q':
            rank = 12
        elif rank == 'K':
            rank = 13
        elif rank == 'A':
            rank = 14
        else:
            rank = int(rank)

        suits[suit].append(rank)

    moves = 0
    for suit in suits.values():
        if suit:
            increasing = all(suit[i] <= suit[i+1] for i in range(len(suit) - 1))
            decreasing = all(suit[i] >= suit[i+1] for i in range(len(suit) - 1))
            moves += min(len(suit) - sum(increasing), len(suit) - sum(decreasing))

    return moves

# Read input
n = int(input())
cards = input().split()

# Output result
print(min_card_moves(n, cards))
