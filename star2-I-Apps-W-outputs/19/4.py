
from collections import defaultdict
from collections import deque

def solve(N, tunnels):
    graph = defaultdict(list)
    for u, v in tunnels:
        graph[u].append(v)
        graph[v].append(u)
    
    queue = deque([1])
    visited = set([1])
    distances = {1: 0}
    
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[curr] + 1
    
    max_controlled = [1] * N
    for planet in range(1, N + 1):
        curr_controlled = 1
        for neighbor in graph[planet]:
            if distances[neighbor] == 1:
                curr_controlled += 1
        max_controlled[curr_controlled] = max(max_controlled[curr_controlled], planet)
    
    return max_controlled

N = int(input())
tunnels = []
for _ in range(N - 1):
    u, v = map(int, input().split())
    tunnels.append((u, v))

max_controlled = solve(N, tunnels)
print(*max_controlled)

