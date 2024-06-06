
from collections import defaultdict
from collections import deque

n = int(input())
v = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(node, visited):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, visited)

def bfs(node):
    visited = [False] * (n + 1)
    queue = deque([node])
    visited[node] = True
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
    return visited

def check(visited):
    for i in range(1, n + 1):
        if not visited[i]:
            return False
    return True

def solve():
    visited = bfs(1)
    if not check(visited):
        return 0
    ans = 1
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited)
            ans *= 2
    return ans

print(solve())
