
from collections import deque


def bfs(adj, s, t):
    q = deque()
    visited = [False] * len(adj)
    q.append(s)
    visited[s] = True
    parent = [None] * len(adj)

    while q:
        u = q.popleft()
        if u == t:
            return parent
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    return parent


def min_settlers(adj, s, t):
    parent = bfs(adj, s, t)
    if not parent[t]:
        return -1

    settlers = 0
    v = t
    while v != s:
        settlers += 1
        v = parent[v]

    return settlers


def main():
    n, m, k = map(int, input().split())
    ore = set(map(int, input().split()))
    coal = set(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for u in range(n):
        a, *neighbours = map(int, input().split())
        for v in neighbours:
            adj[u].append(v - 1)
    settlers = float('inf')
    for u in range(n):
        if u + 1 in ore:
            settlers = min(settlers, min_settlers(adj, u, 0) + 1)
        if u + 1 in coal:
            settlers = min(settlers, min_settlers(adj, u, 0) + 1)

    if settlers == float('inf'):
        print('impossible')
    else:
        print(settlers)


if __name__ == '__main__':
    main()


