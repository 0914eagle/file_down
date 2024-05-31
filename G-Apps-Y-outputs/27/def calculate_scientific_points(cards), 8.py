
def calculate_scientific_points(cards):
    tablet_count = cards.count('T')
    compass_count = cards.count('C')
    gear_count = cards.count('G')

    total_points = tablet_count ** 2 + compass_count ** 2 + gear_count ** 2
    
    min_count = min(tablet_count, compass_count, gear_count)
    total_points += min_count * 7

    return total_points

# Read input
cards = input().strip()

# Calculate and output the scientific points earned
print(calculate_scientific_points(cards))
