
from collections import defaultdict

def count_ways_to_choose_three_people(N, names):
    count_dict = defaultdict(int)
    for name in names:
        count_dict[name[0]] += 1

    total_ways = 0
    for c1 in "MARCH":
        for c2 in "MARCH":
            if c1 == c2 and count_dict[c1] < 2:
                continue
            for c3 in "MARCH":
                if c1 == c3 or c2 == c3:
                    continue
                if count_dict[c3] > 0:
                    total_ways += count_dict[c1] * count_dict[c2] * count_dict[c3]
    
    return total_ways // 6  # Divide by 6 to account for permutation of 3 people

# Read input
N = int(input())
names = [input().strip() for _ in range(N)]

# Calculate and print the result
result = count_ways_to_choose_three_people(N, names)
print(result)
