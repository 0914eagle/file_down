
from sys import stdin
from collections import defaultdict

def dfs(node, parent):
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            labels[node - 1] = max(labels[node - 1], labels[child - 1] + 1)

n = int(stdin.readline())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
labels = [0] * n
dfs(1, -1)
print(*labels, sep='\n')

