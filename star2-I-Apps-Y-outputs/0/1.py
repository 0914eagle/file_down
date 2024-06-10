
from itertools import combinations
n = int(input())
print(sum(1 for i in range(2, n+1) for _ in combinations(range(n), i)))

