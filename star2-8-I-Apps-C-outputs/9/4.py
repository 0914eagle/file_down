

from collections import defaultdict, deque

def dijkstra(graph, start):
    queue = deque([start])
    visited = {start}
    distance = {start: 0}
    
    while queue:
        current = queue.popleft()
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                distance[neighbor] = distance[current] | weight
    
    return distance

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    distance = dijkstra(graph, s)
    print(distance[t])


