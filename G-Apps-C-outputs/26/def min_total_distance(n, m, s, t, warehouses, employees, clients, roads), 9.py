
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))

    distances = {}
    for start in warehouses + employees:
        distances[start] = {node: float('inf') for node in range(1, n+1)}
        distances[start][start] = 0
        heap = [(0, start)]
        while heap:
            dist, current = heapq.heappop(heap)
            if dist > distances[start][current]:
                continue
            for neighbor, edge_dist in graph[current]:
                new_dist = dist + edge_dist
                if new_dist < distances[start][neighbor]:
                    distances[start][neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
    
    total_distance = float('inf')
    for delivery_dest in clients:
        for warehouse in warehouses:
            for employee in employees:
                total_distance = min(total_distance, distances[warehouse][employee] + distances[employee][delivery_dest])

    return total_distance

# Input parsing
n, m, s, t = map(int, input().split())
warehouse1, warehouse2 = map(int, input().split())
warehouses = [warehouse1, warehouse2]
employees = list(map(int, input().split()))
clients = list(map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

result = min_total_distance(n, m, s, t, warehouses, employees, clients, roads)
print(result)
