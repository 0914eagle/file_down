
def calculate_scientific_points(cards):
    counts = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        counts[card] += 1
    
    total_points = 0
    for card, count in counts.items():
        total_points += count ** 2
    
    total_points += min(counts.values()) * 7
    
    return total_points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
