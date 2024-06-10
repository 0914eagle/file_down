
from sys import stdin
from collections import defaultdict
input = stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
tree = defaultdict(set)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].add(v)
    tree[v].add(u)

def dfs(u, parent, color):
    global red, blue
    if a[u] == 1:
        red += 1
    elif a[u] == 2:
        blue += 1
    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u, color)

ans = 0
for u, adj in tree.items():
    if len(adj) == n-1:
        red = 0
        blue = 0
        dfs(u, 0, a[u])
        ans += (red * blue)

print(ans)

