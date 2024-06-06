
from collections import deque

n = int(input())

def bfs(start, fin, adj_list):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        u = queue.popleft()
        for node in adj_list[u]:
            if not visited[node]:
                visited[node] = True
                if node == fin:
                    return True
                queue.append(node)
    return False

adj_list = [[] for _ in range(n + 1)]
for i in range(n):
    _, a, b = list(map(int, input().split()))
    adj_list[i + 1].append(b)
    adj_list[b].append(i + 1)
for _ in range(n):
    _, a, b = list(map(int, input().split()))
    print("YES" if bfs(a, b, adj_list) else "NO")

