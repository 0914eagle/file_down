
from collections import defaultdict

def dfs(node, parent, adj_list, universities, dist):
    if node in universities:
        dist[node] = 0
    for neighbor in adj_list[node]:
        if neighbor != parent:
            dist[node] = max(dist[node], dfs(neighbor, node, adj_list, universities, dist) + 1)
    return dist[node]

def max_distance(n, k, universities, roads):
    adj_list = defaultdict(list)
    for x, y in roads:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    dist = [0] * (n + 1)
    dfs(universities[0], -1, adj_list, set(universities), dist)
    
    max_distances = sorted([dist[u] for u in universities], reverse=True)[:k]
    
    return sum(max_distances)

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

print(max_distance(n, k, universities, roads))
