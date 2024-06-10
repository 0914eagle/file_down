
from collections import Counter
n = int(input())
votes = [input() for _ in range(n)]
counter = Counter(votes)
max_count = max(counter.values())
for s, count in sorted(counter.items()):
    if count == max_count:
        print(s)

