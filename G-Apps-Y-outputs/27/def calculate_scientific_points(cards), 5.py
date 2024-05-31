
def calculate_scientific_points(cards):
    count = {
        'T': 0,
        'C': 0,
        'G': 0
    }
    
    for card in cards:
        count[card] += 1
    
    total_points = 0
    
    for card_type, num_cards in count.items():
        total_points += num_cards**2
    
    total_points += 7 * min(count.values())
    
    return total_points

# Input processing
cards = input().strip()
print(calculate_scientific_points(cards))
