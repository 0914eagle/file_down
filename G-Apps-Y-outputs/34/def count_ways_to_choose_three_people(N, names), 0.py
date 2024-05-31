
def count_ways_to_choose_three_people(N, names):
    counts = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    
    for name in names:
        counts[name[0]] += 1
    
    ways = 0
    for c in counts.values():
        if c >= 3:
            ways += c * (c-1) * (c-2) // 6
        elif c >= 2:
            for other_c in counts.values():
                if other_c > c:
                    ways += c * (c-1) * other_c // 2
        else:
            for other_c in counts.values():
                if other_c > c:
                    for other_c2 in counts.values():
                        if other_c2 > c and other_c2 > other_c:
                            ways += c * other_c * other_c2
    
    return ways

# Input
N = int(input())
names = [input() for _ in range(N)]

# Output
print(count_ways_to_choose_three_people(N, names))
