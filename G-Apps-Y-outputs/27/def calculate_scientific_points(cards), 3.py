
def calculate_scientific_points(cards):
    counts = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        counts[card] += 1

    total_points = 0
    for count in counts.values():
        total_points += count**2

    min_count = min(counts.values())
    total_points += min_count * 7

    return total_points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
