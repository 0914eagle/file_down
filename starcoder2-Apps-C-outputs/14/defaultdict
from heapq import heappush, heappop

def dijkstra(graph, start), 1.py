
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, v = heappop(pq)
        if v in dist and d > dist[v]:
            continue
        for u, w in graph[v]:
            if u not in dist or d + w < dist[u]:
                dist[u] = d + w
                heappush(pq, (d + w, u))
    return dist

def main():
    n, r = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(r):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    f = int(input())
    for _ in range(f):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = dijkstra(graph, 1)
    print(dist[1])

if __name__ == '__main__':
    main()
