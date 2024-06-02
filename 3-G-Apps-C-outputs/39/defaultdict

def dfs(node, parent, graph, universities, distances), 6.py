
from collections import defaultdict

def dfs(node, parent, graph, universities, distances):
    total_distance = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            total_distance += dfs(neighbor, node, graph, universities, distances)
    if node in universities:
        distances[node] = total_distance
    return total_distance + 1

def solve_treeland(n, k, universities, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    distances = {}
    dfs(universities[0], -1, graph, set(universities), distances)

    max_distances = []
    for u in universities:
        max_distances.append(distances[u])

    max_distances.sort(reverse=True)
    return sum(max_distances[:k*2])

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

# Solve the problem
result = solve_treeland(n, k, universities, roads)
print(result)
