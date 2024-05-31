
from collections import defaultdict

def count_ways_to_choose_three_people(N, names):
    count_dict = defaultdict(int)
    for name in names:
        count_dict[name[0]] += 1

    selected_letters = ['M', 'A', 'R', 'C', 'H']
    selected_counts = [count_dict[letter] for letter in selected_letters]

    total_ways = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                total_ways += selected_counts[i] * selected_counts[j] * selected_counts[k]

    return total_ways // 6  # Divide by 6 to account for ordering

# Input
N = int(input())
names = [input().strip() for _ in range(N)]

# Output
print(count_ways_to_choose_three_people(N, names))
