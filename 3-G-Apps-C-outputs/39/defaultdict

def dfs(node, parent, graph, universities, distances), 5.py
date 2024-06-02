
from collections import defaultdict

def dfs(node, parent, graph, universities, distances):
    total_distance = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            total_distance += dfs(neighbor, node, graph, universities, distances)
    
    if node in universities:
        distances.append(total_distance)
        return 0
    else:
        return total_distance + 1

def max_total_distance(n, k, universities, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    distances = []
    dfs(universities[0], -1, graph, set(universities), distances)
    
    distances.sort(reverse=True)
    return sum(distances[:k])

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

# Output
print(max_total_distance(n, k, universities, roads))
