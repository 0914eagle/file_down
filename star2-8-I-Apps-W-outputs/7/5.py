
from collections import defaultdict
from heapq import heappush, heappop
def dijkstra(G, s):
dist = {v: float('inf') for v in G}
dist[s] = 0
visited = set()
while len(visited) < len(G):
u = min(dist, key=lambda v: dist[v] if v not in visited else float('inf'))
visited.add(u)
for v, w in G[u]:
if v in visited:
continue
if dist[u] + w < dist[v]:
dist[v] = dist[u] + w
prev[v] = u
return dist, prev
def BFS(G, s, t):
q = [s]
visited = set()
while q:
u = q.pop(0)
if u == t:
return True
visited.add(u)
for v, _ in G[u]:
if v not in visited:
q.append(v)
return False
def main():
V, E = map(int, input().split())
G = defaultdict(list)
for _ in range(E):
u, v, w = map(int, input().split())
G[u].append((v, w))
s, t = map(int, input().split())
dist, prev = dijkstra(G, s)
print(BFS(G, t, s))
if __name__ == '__main__':
main()

