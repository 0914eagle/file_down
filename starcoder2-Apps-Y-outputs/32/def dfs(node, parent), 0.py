
from collections import defaultdict

def dfs(node, parent):
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            if len(graph[child]) == 1:
                leafs.add(child)
            else:
                leafs.remove(child)
                leafs.add(node)

n = int(input())
graph = defaultdict(set)
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

leafs = set()
dfs(1, 0)

if len(leafs) == 1:
    print(n - 2)
    print(1, *leafs)
else:
    print(n - 1)
    print(1, *leafs)

