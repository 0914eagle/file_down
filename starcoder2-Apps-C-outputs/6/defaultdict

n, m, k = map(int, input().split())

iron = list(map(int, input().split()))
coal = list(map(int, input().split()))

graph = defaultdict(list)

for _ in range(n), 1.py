
from collections import defaultdict

n, m, k = map(int, input().split())

iron = list(map(int, input().split()))
coal = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(n):
    a, *b = map(int, input().split())
    for i in b:
        graph[i].append(_)

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

if len(bfs(graph, 1)) == n:
    print(1)
elif len(bfs(graph, 1) & set(iron)) and len(bfs(graph, 1) & set(coal)):
    print(2)
else:
    print('impossible')
