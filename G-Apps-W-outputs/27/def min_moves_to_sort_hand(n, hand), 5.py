
def min_moves_to_sort_hand(n, hand):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    
    for card in hand:
        rank, suit = card[:-1], card[-1]
        suits[suit].append(rank)
    
    moves = 0
    for suit in suits.values():
        sorted_asc = sorted(suit)
        sorted_desc = sorted(suit, reverse=True)
        moves += min(len(suit) - sum(rank == sorted_asc[i] for i, rank in enumerate(suit)),
                     len(suit) - sum(rank == sorted_desc[i] for i, rank in enumerate(suit)))
    
    return moves

# Reading input
n = int(input())
hand = input().split()

# Calling the function and outputting the result
print(min_moves_to_sort_hand(n, hand))
