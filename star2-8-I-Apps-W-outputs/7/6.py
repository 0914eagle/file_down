
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(G, s):
dist = defaultdict(lambda : float("inf"))
dist[s] = 0
pq = []
heappush(pq, (0, s))
while pq:
cur_dist, cur_v = heappop(pq)
if cur_dist > dist[cur_v]: continue
for nxt_v, nxt_dist in G[cur_v]:
if cur_dist + nxt_dist < dist[nxt_v]:
dist[nxt_v] = cur_dist + nxt_dist
heappush(pq, (dist[nxt_v], nxt_v))
return dist

V, E = map(int, input().split())
G = defaultdict(list)
for _ in range(E):
u, v, w = map(int, input().split())
G[u].append((v, w))

s, t = map(int, input().split())
dist = dijkstra(G, s)
if dist[t] == float("inf"):
print(0)
else:
print(len(dist[t]))

