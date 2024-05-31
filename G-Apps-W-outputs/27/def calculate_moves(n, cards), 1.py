
def calculate_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    
    for card in cards:
        rank, suit = card[:-1], card[-1]
        if rank.isdigit():
            rank = int(rank)
        else:
            rank = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]

        suits[suit].append(rank)

    moves = 0
    for suit in suits.values():
        asc = sorted(suit)
        desc = sorted(suit, reverse=True)
        
        moves += min(len(suit) - sum(suit[i] == asc[i] for i in range(len(suit))),
                     len(suit) - sum(suit[i] == desc[i] for i in range(len(suit)))

    return moves

n = int(input())
cards = input().split()
print(calculate_moves(n, cards))
