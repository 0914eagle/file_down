
n, m, k = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    x, y, w = map(int, input().split())
    graph[x - 1].append((y - 1, w))
    graph[y - 1].append((x - 1, w))
routes = []
for i in range(k):
    a, b = map(int, input().split())
    routes.append((a - 1, b - 1))
def dijkstra(graph, start):
    dist = [float("inf")] * len(graph)
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        cur_dist, cur_v = heapq.heappop(queue)
        if cur_dist > dist[cur_v]:
            continue
        for neighbour, weight in graph[cur_v]:
            if cur_dist + weight < dist[neighbour]:
                dist[neighbour] = cur_dist + weight
                heapq.heappush(queue, (dist[neighbour], neighbour))
    return dist
min_cost = float("inf")
for i in range(m):
    x, y, w = map(int, input().split())
    x, y = x - 1, y - 1
    dist = dijkstra(graph, x)
    min_cost = min(min_cost, sum(dist[a] for a, b in routes) - w)
    graph[x].remove((y, w))
    graph[y].remove((x, w))
    graph[x].append((y, 0))
    graph[y].append((x, 0))
    dist = dijkstra(graph, x)
    min_cost = min(min_cost, sum(dist[a] for a, b in routes))
    graph[x].remove((y, 0))
    graph[y].remove((x, 0))
    graph[x].append((y, w))
    graph[y].append((x, w))
print(min_cost)

