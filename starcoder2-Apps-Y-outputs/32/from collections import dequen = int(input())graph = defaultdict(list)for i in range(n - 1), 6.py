
from collections import defaultdict
from collections import deque

n = int(input())

graph = defaultdict(list)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

def find_farthest_node(graph, root):
    visited = bfs(graph, root)
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return vertex

a = find_farthest_node(graph, 1)
b = find_farthest_node(graph, a)
c = find_farthest_node(graph, b)

print(len(bfs(graph, a)) + len(bfs(graph, b)) + len(bfs(graph, c)) - 6)
print(a, b, c)

