
from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

def check_bfs(graph, start, sequence):
    visited = bfs(graph, start)
    if len(visited) != len(graph):
        return False
    for i, v in enumerate(sequence):
        if v not in graph[i+1]:
            return False
    return True

n = int(input())
graph = {i+1: set() for i in range(n)}
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)
sequence = list(map(int, input().split()))

print("Yes" if check_bfs(graph, 1, sequence) else "No")

