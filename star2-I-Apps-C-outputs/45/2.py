
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    used = [False] * (len(graph) + 1)
    used[start] = True
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if not used[neighbor]:
                used[neighbor] = True
                queue.append(neighbor)
    return result


def check_bfs(graph, start, sequence):
    bfs_sequence = bfs(graph, start)
    return bfs_sequence == sequence


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
sequence = list(map(int, input().split()))
print("Yes" if check_bfs(graph, 1, sequence) else "No")

