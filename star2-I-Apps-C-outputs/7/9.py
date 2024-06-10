
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    while pq:
        curr_dist, curr_node = heappop(pq)
        if curr_node == end:
            return curr_dist
        for neighbor, cost in graph[curr_node]:
            if curr_dist + cost < dist[neighbor]:
                dist[neighbor] = curr_dist + cost
                heappush(pq, (dist[neighbor], neighbor))
    return float('inf')

def main():
    n, m, p = map(int, input().split())
    insecure = set(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(m):
        x, y, l = map(int, input().split())
        graph[x].append((y, l))
        graph[y].append((x, l))
    cost = 0
    for i in range(1, n + 1):
        if i in insecure:
            continue
        curr_cost = dijkstra(graph, i, insecure.pop())
        if curr_cost == float('inf'):
            print('impossible')
            return
        cost += curr_cost
        insecure.add(i)
    print(cost)

if __name__ == '__main__':
    main()

