
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur_node = heappop(pq)
        for neighbor, weight in graph[cur_node]:
            if cur_dist + weight < dist[neighbor]:
                dist[neighbor] = cur_dist + weight
                heappush(pq, (dist[neighbor], neighbor))
    return dist

def main():
    n, m, k = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        x, y, w = map(int, input().split())
        graph[x].append((y, w))
        graph[y].append((x, w))
    routes = []
    for _ in range(k):
        a, b = map(int, input().split())
        routes.append((a, b))
    min_cost = float('inf')
    for i in range(m):
        x, y, w = map(int, input().split())
        graph[x].remove((y, w))
        graph[y].remove((x, w))
        graph[x].append((y, 0))
        graph[y].append((x, 0))
        total_cost = 0
        for a, b in routes:
            dist = dijkstra(graph, a)
            total_cost += dist[b]
        min_cost = min(min_cost, total_cost)
        graph[x].remove((y, 0))
        graph[y].remove((x, 0))
        graph[x].append((y, w))
        graph[y].append((x, w))
    print(min_cost)

if __name__ == '__main__':
    main()

