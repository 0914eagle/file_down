
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def max_connected_towers(n, towers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if distance(towers[i][0], towers[i][1], towers[j][0], towers[j][1]) <= 2:
                graph[i].append(j)
                graph[j].append(i)

    max_towers = 0
    for i in range(n):
        visited = [False] * n
        dfs(i, visited, graph)
        max_towers = max(max_towers, sum(visited))

    return max_towers

# Input processing
n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

# Calculate and output the result
print(max_connected_towers(n, towers))
