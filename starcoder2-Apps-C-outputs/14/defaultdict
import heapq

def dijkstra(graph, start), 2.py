
from collections import defaultdict
import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node in dist and current_dist > dist[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if neighbor not in dist or distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist

def main():
    n, r = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(r):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    f = int(input())
    for _ in range(f):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    dist = dijkstra(graph, 1)
    print(dist[1])

if __name__ == '__main__':
    main()
