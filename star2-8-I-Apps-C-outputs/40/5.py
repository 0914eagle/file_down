
from collections import defaultdict
import heapq

def dijkstra(graph, source, target):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_node == target:
            return dist[target]
        for neighbor, weight in graph[curr_node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return -1

def main():
    n, m, alpha = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))
    min_energy = float('inf')
    for i in range(1, n + 1):
        energy = dijkstra(graph, i, i)
        if energy != -1:
            min_energy = min(min_energy, energy + alpha)
    if min_energy == float('inf'):
        print('Poor girl')
    else:
        print(min_energy)

if __name__ == '__main__':
    main()

