
import heapq

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w, len(graph[v])))
        graph[v].append((u, 0, -w, len(graph[u])-1))

    def dijkstra():
        dist = [float('inf')] * n
        dist[s] = 0
        parent = [-1] * n
        in_queue = [False] * n
        pq = [(0, s)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            in_queue[u] = False
            
            for v, cap, cost, rev in graph[u]:
                if cap > 0 and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    parent[v] = (u, rev)
                    if not in_queue[v]:
                        heapq.heappush(pq, (dist[v], v))
                        in_queue[v] = True
        
        return dist[t], parent

    flow, cost = 0, 0
    while True:
        dist, parent = dijkstra()
        if dist == float('inf'):
            break
        
        f = float('inf')
        v = t
        while v != s:
            u, rev = parent[v]
            f = min(f, graph[u][rev][1])
            v = u
        
        flow += f
        cost += f * dist
        
        v = t
        while v != s:
            u, rev = parent[v]
            graph[u][rev] = (graph[u][rev][0], graph[u][rev][1] - f, graph[u][rev][2], graph[u][rev][3])
            graph[v][graph[u][rev][3]] = (graph[v][graph[u][rev][3]][0], graph[v][graph[u][rev][3]][1] + f, graph[v][graph[u][rev][3]][2], graph[v][graph[u][rev][3]][3])
            v = u
    
    return flow, cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
max_flow, min_cost = min_cost_max_flow(n, m, s, t, edges)
print(max_flow, min_cost)
