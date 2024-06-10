
from collections import defaultdict

def dfs(node, parent, graph, labels):
    for child in graph[node]:
        if child != parent:
            labels[child] = labels[node] + 1
            dfs(child, node, graph, labels)

def solve(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    labels = [0] * (n + 1)
    dfs(1, -1, graph, labels)
    
    return labels[1:]

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

labels = solve(n, edges)
print(*labels, sep="\n")

