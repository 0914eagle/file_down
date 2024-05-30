
import heapq
from collections import defaultdict

def dijkstra(adj_list, start):
    dist = {node: float('inf') for node in adj_list}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > dist[cur_node]:
            continue

        for neighbor, weight in adj_list[cur_node]:
            new_dist = cur_dist | weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist

# Read input
n, m = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    adj_list[a].append((b, w))
    adj_list[b].append((a, w))

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    # Run Dijkstra's algorithm with bitwise OR operation on road lengths
    dist = dijkstra(adj_list, s)
    print(dist[t])

```
