
def card_sorting_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    moves = 0

    for card in cards:
        rank, suit = card[:-1], card[-1]
        suits[suit].append(rank)

    for suit in suits.values():
        ascending_moves = 0
        descending_moves = 0
        prev_rank = None

        for rank in suit:
            if prev_rank is not None:
                if rank > prev_rank:
                    ascending_moves += 1
                else:
                    descending_moves += 1

            prev_rank = rank

        moves += min(ascending_moves, descending_moves)

    return moves

# Read input
n = int(input())
cards = input().split()

# Calculate and output the minimum number of moves
print(card_sorting_moves(n, cards))
