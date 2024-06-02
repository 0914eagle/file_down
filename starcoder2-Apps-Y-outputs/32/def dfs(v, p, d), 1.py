
from collections import defaultdict

def dfs(v, p, d):
    d[v] = d[p] + 1
    for u in g[v]:
        if u != p:
            dfs(u, v, d)

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

d = defaultdict(int)
dfs(1, 0, d)

mx = max(d.values())
v = [k for k, v in d.items() if v == mx]

if len(v) == 1:
    print(mx - 1)
    print(v[0], 1, 1)
else:
    print(mx)
    print(v[0], v[1], 1)

