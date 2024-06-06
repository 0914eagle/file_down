
from itertools import combinations

n, k = map(int, input().split())
coins = list(map(int, input().split()))

ans = []

for c in range(1, n + 1):
    for comb in combinations(coins, c):
        if sum(comb) <= k and sum(comb) not in ans:
            ans.append(sum(comb))

print(len(ans))
for i in sorted(ans):
    print(i, end=' ')
