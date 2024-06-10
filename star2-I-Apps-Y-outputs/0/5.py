
from itertools import combinations
n = int(input())
print(sum(1 for _ in combinations(range(n), 2)))

