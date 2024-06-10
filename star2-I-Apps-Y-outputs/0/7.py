
from itertools import combinations

n = int(input())

if n == 0 or n == 1:
    print(0)
else:
    print(sum(1 for _ in combinations(range(n), 2)))

