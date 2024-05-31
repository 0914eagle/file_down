
def card_sorting_moves(n, cards):
    suits = {'s': [], 'h': [], 'd': [], 'c': []}
    
    for card in cards:
        rank, suit = card[:-1], card[-1]
        suits[suit].append(rank)
    
    total_moves = 0
    for suit in suits.values():
        ascending_moves = descending_moves = 0
        sorted_suit = sorted(suit, key=lambda x: ('A23456789TJQK'.index(x[0]), x[1]))
        
        for i in range(len(suit)):
            if suit[i] != sorted_suit[i]:
                ascending_moves += 1
        for i in range(len(suit)):
            if suit[i] != sorted_suit[-(i+1)]:
                descending_moves += 1
        
        total_moves += min(ascending_moves, descending_moves)
    
    return total_moves

# Input parsing
n = int(input())
cards = input().split()

print(card_sorting_moves(n, cards))
