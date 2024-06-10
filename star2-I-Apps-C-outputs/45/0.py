
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        vertex = queue.popleft()
        yield vertex
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
sequence = list(map(int, input().split()))

for i, vertex in enumerate(bfs(graph, 1), 1):
    if vertex != sequence[i - 1]:
        print("No")
        break
else:
    print("Yes")

