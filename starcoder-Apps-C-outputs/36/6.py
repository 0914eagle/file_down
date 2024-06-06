
# your code goes here
from collections import defaultdict
from collections import deque
import math

def make_graph(m):
    graph = defaultdict(list)
    for i in range(m):
        b = map(int, input().strip().split())
        x = list(b)
        x = x[1:]
        for i in range(0, len(x) - 1, 2):
            graph[x[i]].append(x[i + 1])
            graph[x[i + 1]].append(x[i])
    return graph

def BFS(graph, start, visited):
    visited.add(start)
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
graph = make_graph(m)

for i in range(1, n+1):
    visited = set()
    if arr[i-1] == 0:
        if len(BFS(graph, i, visited)) == n:
            print("NO")
            break
else:
    print("YES")
