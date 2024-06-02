
def calculate_scientific_points(cards):
    card_counts = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        card_counts[card] += 1
    
    total_points = 0
    for card_type, count in card_counts.items():
        total_points += count**2
    
    total_points += min(card_counts.values()) * 7
    
    return total_points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
