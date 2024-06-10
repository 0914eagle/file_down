
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heappush(pq, (dist[v], v))
    return dist, prev

def get_path(prev, start, end):
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = prev[curr]
    path.append(start)
    return path[::-1]

def solve(n, m, s, t, roads):
    graph = defaultdict(list)
    for a, b, l in roads:
        graph[a].append((b, l))
    
    dist, prev = dijkstra(graph, s)
    
    for a, b, l in roads:
        if dist[b] == dist[a] + l:
            print('YES')
        elif dist[b] > dist[a] + l:
            print('CAN', l - (dist[b] - dist[a]))
        else:
            print('NO')

if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, l = map(int, input().split())
        roads.append((a, b, l))
    
    solve(n, m, s, t, roads)

