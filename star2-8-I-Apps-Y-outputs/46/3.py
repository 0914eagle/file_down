
from collections import Counter

n = int(input())
votes = [input() for _ in range(n)]

counter = Counter(votes)
max_count = max(counter.values())
for k, v in sorted(counter.items()):
    if v == max_count:
        print(k)

