
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def check_bfs(graph, start, sequence):
    visited = bfs(graph, start)
    if len(visited) != len(graph):
        return False
    for vertex in sequence:
        if vertex not in visited:
            return False
    return True

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
sequence = list(map(int, input().split()))

print("Yes" if check_bfs(graph, 1, sequence) else "No")

