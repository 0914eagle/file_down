
def dijkstra(graph, start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr = heapq.heappop(pq)
        
        for neighbor, weight in graph[curr]:
            new_dist = curr_dist | weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    return dist
    
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, w))
    graph[b].append((a, w))
    
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    
    print(dijkstra(graph, s)[t])

