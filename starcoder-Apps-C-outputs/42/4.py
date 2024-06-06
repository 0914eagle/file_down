
import sys
from collections import defaultdict as dd

n = int(sys.stdin.readline())

d = dd(list)

for i in range(n):
    for j,v in enumerate(map(int,sys.stdin.readline().split())):
        if v:
            d[v].append(i+1)

ans = []
for k,v in d.items():
    if len(v) != 2:
        ans.append(k)
    else:
        ans.append(v[0])
        ans.append(v[1])

ans.sort()

print(*ans)
