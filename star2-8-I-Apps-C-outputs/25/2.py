
from collections import deque

def solve():
    n, m, k = map(int, input().split())
    ores = set(map(int, input().split()))
    coals = set(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for i in range(n):
        a, *b = map(int, input().split())
        adj[i] = b
    q = deque([1])
    ore_dist = [-1] * n
    ore_dist[0] = 0
    while q:
        cur = q.popleft()
        for neighbour in adj[cur - 1]:
            if ore_dist[neighbour - 1] == -1:
                ore_dist[neighbour - 1] = ore_dist[cur - 1] + 1
                q.append(neighbour)
    q = deque([1])
    coal_dist = [-1] * n
    coal_dist[0] = 0
    while q:
        cur = q.popleft()
        for neighbour in adj[cur - 1]:
            if coal_dist[neighbour - 1] == -1:
                coal_dist[neighbour - 1] = coal_dist[cur - 1] + 1
                q.append(neighbour)
    best = float('inf')
    for i in range(n):
        if ore_dist[i] != -1 and coal_dist[i] != -1:
            best = min(best, ore_dist[i] + coal_dist[i] + 1)
    if best == float('inf'):
        print('impossible')
    else:
        print(best)

solve()

