
def calculate_scientific_points(cards):
    counts = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        counts[card] += 1

    total_points = 0
    for value in counts.values():
        total_points += value**2

    min_count = min(counts.values())
    bonus_points = min_count * 7

    return total_points + bonus_points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
