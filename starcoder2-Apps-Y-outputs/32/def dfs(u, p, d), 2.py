
from collections import defaultdict

def dfs(u, p, d):
    d[u] = d[p] + 1
    for v in g[u]:
        if v == p:
            continue
        dfs(v, u, d)

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

d1 = defaultdict(int)
d2 = defaultdict(int)
dfs(1, 0, d1)
dfs(n, 0, d2)

mx = 0
a = 0
b = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        if d1[i] + d2[j] > mx:
            mx = d1[i] + d2[j]
            a = i
            b = j

print(mx)
print(a, b, 1)

