
from sys import stdin

def dfs(v, p, c):
    cc[c][0] += 1
    cc[c][1] += a[v]
    
    for u in tree[v]:
        if u != p:
            dfs(u, v, c)

def dfs1(v, p, c):
    res[c] += cc[c][0] - 1
    
    for u in tree[v]:
        if u != p:
            cc[c][0] -= 1
            cc[c][1] -= a[u]
            dfs1(u, v, c)
            cc[c][0] += 1
            cc[c][1] += a[u]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v, u = map(int, stdin.readline().split())
    tree[v].append(u)
    tree[u].append(v)
    
res = [0] * 3
cc = [[0, 0] for _ in range(3)]

dfs(1, 0, 1)
dfs1(1, 0, 1)

print(res[1])

