
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
d = defaultdict(list)
for i, v in enumerate(a):
  d[v].append(i + 1)

ans = 0
for v in d:
  for i in d[v]:
    for j in d[2*v]:
      if i != j:
        ans += 1
print(ans)

