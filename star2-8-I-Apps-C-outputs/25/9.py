
from collections import deque
def find_path(graph, start, end):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex == end:
            return True
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return False
def get_connected_cells(graph, start, resource):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex in resource:
            return True
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return False
def steel_age(n, m, k, ore, coal, graph):
    if n == 1:
        return "impossible"
    if m == 0 or k == 0:
        return "impossible"
    if find_path(graph, 1, ore[0]) and find_path(graph, 1, coal[0]):
        return 1
    if get_connected_cells(graph, ore[0], coal):
        return 1
    return 2

n, m, k = map(int, input().split())
ore = list(map(int, input().split()))
coal = list(map(int, input().split()))
graph = {}
for i in range(1, n+1):
    graph[i] = []
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        graph[i].append(a[j])
print(steel_age(n, m, k, ore, coal, graph))

