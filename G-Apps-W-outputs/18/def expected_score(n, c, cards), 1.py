
from itertools import combinations

def expected_score(n, c, cards):
    total_score = 0.0
    total_combinations = 0
    
    for drawn_cards in combinations(cards, c):
        max_drawn_card = max(drawn_cards)
        remaining_cards = [card for card in cards if card > max_drawn_card]
        
        if len(remaining_cards) == 0:
            total_score += max(cards)
        else:
            total_score += max(remaining_cards)
        
        total_combinations += 1
    
    return total_score / total_combinations

# Read input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Calculate and output expected score
print("{:.6f}".format(expected_score(n, c, cards)))
