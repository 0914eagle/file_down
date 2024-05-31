
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))

    def dijkstra(start):
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for neighbor, edge_dist in graph[node]:
                new_dist = dist + edge_dist
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return distances

    warehouse1 = dijkstra(warehouses[0])
    warehouse2 = dijkstra(warehouses[1])

    min_distance = float('inf')
    for employee in employees:
        for client in clients:
            distance = min(warehouse1[employee] + warehouse2[client], warehouse1[client] + warehouse2[employee])
            if distance < min_distance:
                min_distance = distance

    return min_distance

# Reading input
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_total_distance(n, m, s, t, warehouses, employees, clients, roads))
