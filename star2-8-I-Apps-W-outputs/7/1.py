
from collections import defaultdict, deque

def shortest_path_count(graph, start, end):
queue = deque([start])
visited = set([start])
distance = {start: 0}

while queue:
vertex = queue.popleft()
for neighbor in graph[vertex]:
if neighbor not in visited:
visited.add(neighbor)
distance[neighbor] = distance[vertex] + 1
queue.append(neighbor)
if neighbor == end:
return len(visited)

if __name__ == "__main__":
vertices, edges = map(int, input().split())
graph = defaultdict(list)
for _ in range(edges):
u, v, w = map(int, input().split())
graph[u].append(v)

start, end = map(int, input().split())

print(shortest_path_count(graph, start, end))

