
def calculate_scientific_points(cards):
    card_count = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        card_count[card] += 1
    
    total_points = 0
    for card_type, count in card_count.items():
        total_points += count ** 2
    
    total_points += min(card_count.values()) * 7
    
    return total_points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
