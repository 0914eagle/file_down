
import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))

    return dist

def main():
    n, m, k = map(int, input().split())
    graph = {i+1: {} for i in range(n)}
    roads = []

    for _ in range(m):
        x, y, w = map(int, input().split())
        graph[x][y] = w
        graph[y][x] = w
        roads.append((x, y, w))

    courier_routes = [tuple(map(int, input().split())) for _ in range(k)]

    min_cost = float('inf')

    for i in range(m):
        x, y, _ = roads[i]
        graph[x][y] = 0
        graph[y][x] = 0

        total_cost = 0
        for a, b in courier_routes:
            dist = dijkstra(graph, a)
            total_cost += dist[b]

        min_cost = min(min_cost, total_cost)

        graph[x][y] = roads[i][2]
        graph[y][x] = roads[i][2]

    print(min_cost)


if __name__ == "__main__":
    main()
```
