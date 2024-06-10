
from sys import stdin
from collections import defaultdict

def dfs(node, parent):
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            max_mex[node] = max(max_mex[node], max_mex[child] + 1)

n = int(stdin.readline())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
max_mex = [0] * (n + 1)
dfs(1, -1)
print(*max_mex[1:], sep='\n')

