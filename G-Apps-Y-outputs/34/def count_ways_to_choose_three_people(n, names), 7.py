
def count_ways_to_choose_three_people(n, names):
    counts = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for name in names:
        first_letter = name[0]
        if first_letter in counts:
            counts[first_letter] += 1

    total_ways = 0
    for count in counts.values():
        if count >= 3:
            total_ways += count * (count - 1) * (count - 2) // 6
        else:
            total_ways += count * (count - 1) // 2 * sum([other_count for other_count in counts.values() if other_count > 1 and other_count != count])

    return total_ways

# Input
n = int(input())
names = [input().strip() for _ in range(n)]

# Output
print(count_ways_to_choose_three_people(n, names))
