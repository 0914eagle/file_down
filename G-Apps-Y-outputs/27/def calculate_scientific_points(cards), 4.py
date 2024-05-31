
def calculate_scientific_points(cards):
    counts = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        counts[card] += 1

    points = counts['T']**2 + counts['C']**2 + counts['G']**2
    points += min(counts.values()) * 7

    return points

# Input
cards = input().strip()

# Output
print(calculate_scientific_points(cards))
