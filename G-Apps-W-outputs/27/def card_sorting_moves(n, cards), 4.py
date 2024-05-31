
def card_sorting_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    
    for card in cards:
        rank, suit = card[:-1], card[-1]
        suits[suit].append(rank)
    
    moves = 0
    
    for suit, ranks in suits.items():
        ascending = sorted(ranks)
        descending = sorted(ranks, reverse=True)
        
        moves += min(
            sum(1 for x, y in zip(ranks, ascending) if x != y),
            sum(1 for x, y in zip(ranks, descending) if x != y)
        )
    
    return moves

# Read input
n = int(input())
cards = input().split()

# Call the function and output the result
print(card_sorting_moves(n, cards))
