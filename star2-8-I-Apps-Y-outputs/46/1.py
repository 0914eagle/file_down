
from collections import defaultdict

n = int(input())
counts = defaultdict(int)
for _ in range(n):
    s = input()
    counts[s] += 1
max_count = max(counts.values())
for s, count in counts.items():
    if count == max_count:
        print(s)

