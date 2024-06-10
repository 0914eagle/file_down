
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur_node = heappop(pq)
        if cur_dist > dist[cur_node]:
            continue
        for neighbor, weight in graph[cur_node]:
            if cur_dist + weight < dist[neighbor]:
                dist[neighbor] = cur_dist + weight
                heappush(pq, (dist[neighbor], neighbor))
    return dist


def solve(n, m, k, roads, routes):
    graph = defaultdict(list)
    for x, y, w in roads:
        graph[x].append((y, w))
        graph[y].append((x, w))
    
    min_cost = 0
    for a, b in routes:
        dist = dijkstra(graph, a)
        min_cost += dist[b]
    
    return min_cost


def main():
    n, m, k = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    routes = [tuple(map(int, input().split())) for _ in range(k)]
    
    print(solve(n, m, k, roads, routes))


if __name__ == '__main__':
    main()

