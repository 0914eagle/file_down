
def cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    # Construct a graph of transfer partnerships
    graph = {}
    for a, b, c in partnerships:
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = c
        graph[b][a] = c

    # Dijkstra's algorithm to find shortest path with extra fee
    def dijkstra(start, end, extra_fee):
        from heapq import heappush, heappop
        pq = [(0, start)]
        dist = {node: float('inf') for node in graph}
        dist[start] = 0

        while pq:
            cost, node = heappop(pq)
            if node == end:
                return dist[end]

            if dist[node] < cost:
                continue

            for neighbor, neighbor_cost in graph[node].items():
                new_cost = cost + neighbor_cost
                if new_cost + extra_fee < dist[neighbor]:
                    dist[neighbor] = new_cost + extra_fee
                    heappush(pq, (new_cost + extra_fee, neighbor))

        return float('inf')

    # Find the minimum extra fee for SWERC to provide cheapest transfer
    min_fee = float('inf')
    for i in range(M):
        for j in range(i + 1, M):
            extra_fee = dijkstra(swerc_banks[i], swerc_banks[j], 0)
            min_fee = min(min_fee, extra_fee)

    if min_fee == float('inf'):
        return "Impossible"
    elif min_fee >= 10**9:
        return "Infinity"
    else:
        return min_fee

# Input reading
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
swerc_banks = list(map(int, input().split())

print(cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))
```
