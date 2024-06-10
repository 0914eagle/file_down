
class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v, w in edges:
            self.adj[u - 1].append((v - 1, w))
            self.adj[v - 1].append((u - 1, w))
    
    def dijkstra(self, s):
        dist = [float("inf") for _ in range(self.n)]
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if dist[u] < d:
                continue
            for v, w in self.adj[u]:
                if dist[u] | w < dist[v]:
                    dist[v] = dist[u] | w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))
    
    g = Graph(n, edges)
    
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        print(g.dijkstra(s - 1)[t - 1])
    
if __name__ == "__main__":
    main()

