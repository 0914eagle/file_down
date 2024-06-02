
from collections import defaultdict

def dfs(node, parent, graph, universities, distances):
    total_dist = 0
    for child in graph[node]:
        if child != parent:
            child_dist = dfs(child, node, graph, universities, distances)
            total_dist += child_dist
    if node in universities:
        distances[node] = total_dist
        return 0
    return total_dist + 1

def solve(n, k, universities, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    distances = {}
    dfs(universities[0], -1, graph, set(universities), distances)
    
    max_distances = sorted(distances.values(), reverse=True)[:k]
    return sum(max_distances)

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

# Solve the problem and print the output
print(solve(n, k, universities, roads))
