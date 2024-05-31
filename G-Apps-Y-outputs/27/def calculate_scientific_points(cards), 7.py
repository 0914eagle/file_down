
def calculate_scientific_points(cards):
    counts = {'T': 0, 'C': 0, 'G': 0}
    points = 0
    
    for card in cards:
        counts[card] += 1

    for count in counts.values():
        points += count**2

    min_count = min(counts.values())
    bonus_points = min_count * 7

    total_points = points + bonus_points
    return total_points

# Read input
input_string = input().strip()

# Calculate and output result
print(calculate_scientific_points(input_string))
