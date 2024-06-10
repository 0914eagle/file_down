
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    used = set([start])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in used:
                queue.append(neighbor)
                used.add(neighbor)
    return result


def is_bfs(graph, start, sequence):
    bfs_result = bfs(graph, start)
    return bfs_result == sequence


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
sequence = list(map(int, input().split()))
print("Yes" if is_bfs(graph, 1, sequence) else "No")

