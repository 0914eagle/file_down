
from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)

def dfs(u):
    global adj, visited, color, cycle, timing
    visited[u] = True
    timing += 1
    discovery_time[u] = timing
    color[u] = 1
    for v in adj[u]:
        if not visited[v]:
            dfs(v)
        elif color[v] == 1:
            cycle = True
    color[u] = 2
    timing += 1
    finish_time[u] = timing


def find_cycle():
    global adj, visited, color, cycle, timing
    visited = [False] * (N+1)
    color = [0] * (N+1)
    cycle = False
    timing = 0
    discovery_time = [0] * (N+1)
    finish_time = [0] * (N+1)
    for u in range(1, N+1):
        if not visited[u]:
            dfs(u)

    return cycle


N, K, M = map(int, input().split())
adj = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

is_cycle = find_cycle()
if is_cycle:
    print(0)
else:
    print(K)

