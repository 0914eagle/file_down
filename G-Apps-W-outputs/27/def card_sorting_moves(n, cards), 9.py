
def card_sorting_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    moves = 0

    for card in cards:
        rank, suit = card[:-1], card[-1]
        suits[suit].append(rank)

    for suit in suits.values():
        ascending = sorted(suit)
        descending = sorted(suit, reverse=True)

        moves += min(len(suit) - sum(rank == ascending[i] for i, rank in enumerate(suit)),
                     len(suit) - sum(rank == descending[i] for i, rank in enumerate(suit)))

    return moves

# Input handling
n = int(input())
cards = input().split()

# Call the function and output the result
print(card_sorting_moves(n, cards))
