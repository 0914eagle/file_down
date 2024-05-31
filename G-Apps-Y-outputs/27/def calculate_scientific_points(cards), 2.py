
def calculate_scientific_points(cards):
    count = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        count[card] += 1
    
    total_points = 0
    for card, num in count.items():
        total_points += num**2
    
    total_points += min(count.values()) * 7
    
    return total_points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
