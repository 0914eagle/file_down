
from collections import defaultdict

def max_distance(n, k, universities, roads):
    adj_list = defaultdict(list)
    for x, y in roads:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                distances[neighbor] = distances[node] + 1
                dfs(neighbor, node)
    
    dfs(universities[0], 0)
    
    max_dist = 0
    farthest_node = universities[0]
    for i in range(1, 2*k, 2):
        if distances[universities[i]] > max_dist:
            max_dist = distances[universities[i]]
            farthest_node = universities[i]
    
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    
    dfs(farthest_node, 0)
    
    return max(distances)

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

print(max_distance(n, k, universities, roads))
