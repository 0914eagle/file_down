
from collections import defaultdict

def dfs(node, parent, graph, universities, dist):
    if node in universities:
        dist[node] = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, universities, dist)
            dist[node] = max(dist[node], dist[neighbor] + 1)

def solve():
    n, k = map(int, input().split())
    universities = set(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    dist = {}
    dfs(1, -1, graph, universities, dist)
    
    max_distances = sorted([dist[u] for u in universities], reverse=True)
    ans = sum(max_distances[:k]) + k
    print(ans)

solve()
