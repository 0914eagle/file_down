
from sys import stdin
input = stdin.readline

def bfs(adj, root):
    queue = [root]
    dist = [float("inf") for _ in range(len(adj))]
    dist[root] = 0
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

n = int(input())
l = int(input())
walk = [int(x) for x in input().split()]
adj = [[] for _ in range(n)]
for i in range(n):
    neighbours = [int(x) for x in input().split()]
    for j in range(1, neighbours[0] + 1):
        adj[i].append(neighbours[j])

dist = bfs(adj, walk[0])
sentry_dist = bfs(adj, walk[-1])

chance = 1
for i in walk:
    chance *= 1 - (1 / (dist[i] + sentry_dist[i] + 1))

print(chance)

