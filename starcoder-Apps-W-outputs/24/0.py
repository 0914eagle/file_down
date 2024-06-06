
from itertools import combinations
from collections import Counter

n = int(input())
w = [int(input()) for _ in range(2**n)]

c = Counter(w)
if len(c) < 2**n:
    print('impossible')
    exit()

seen = set()
for x in c:
    if x in seen:
        continue
    seen.add(x)
    for i in range(2, n+1):
        for comb in combinations(w, i):
            if sum(comb) == x:
                w.remove(x)
                break
print('\n'.join(map(str, sorted(w))))
