
from collections import defaultdict
from collections import deque

n = int(input())

graph = defaultdict(list)

for i in range(n - 1):
    a, b, z = map(int, input().split())
    graph[a].append((b, z))
    graph[b].append((a, z))

order = list(map(int, input().split()))

visited = set()

def bfs(start):
    queue = deque()
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        for child, z in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

bfs(1)

if len(visited) == n:
    print(n - 1)
else:
    print(0)

for i in range(n - 1):
    a, b, z = graph[order[i]]
    graph[a].remove((b, z))
    graph[b].remove((a, z))
    visited.clear()
    bfs(1)
    if len(visited) == n:
        print(n - 1)
    else:
        print(0)
