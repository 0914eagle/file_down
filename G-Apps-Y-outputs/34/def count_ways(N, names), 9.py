
from collections import Counter

def count_ways(N, names):
    count = Counter([name[0] for name in names])
    total_ways = 0

    for start_letter in ['M', 'A', 'R', 'C', 'H']:
        if count[start_letter] >= 3:
            total_ways += count[start_letter] * (count[start_letter]-1) * (count[start_letter]-2) // 6

    return total_ways

# Read input
N = int(input())
names = []
for _ in range(N):
    names.append(input().strip())

# Calculate and print the number of ways
print(count_ways(N, names))
