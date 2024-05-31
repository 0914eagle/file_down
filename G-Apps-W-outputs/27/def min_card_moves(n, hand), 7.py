
def min_card_moves(n, hand):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    
    for card in hand:
        rank, suit = card[:-1], card[-1]
        if rank.isdigit():
            rank = int(rank)
        elif rank == 'T':
            rank = 10
        elif rank == 'J':
            rank = 11
        elif rank == 'Q':
            rank = 12
        elif rank == 'K':
            rank = 13
        else:
            rank = 14
        
        suits[suit].append(rank)
    
    total_moves = 0
    for suit in suits.values():
        if suit:
            ascending = sorted(suit)
            descending = sorted(suit, reverse=True)
            moves_ascending = sum(abs(rank - ascending[i]) for i, rank in enumerate(suit))
            moves_descending = sum(abs(rank - descending[i]) for i, rank in enumerate(suit))
            total_moves += min(moves_ascending, moves_descending)
    
    return total_moves

# Input parsing
n = int(input())
hand = input().split()

# Call function and output result
print(min_card_moves(n, hand))
