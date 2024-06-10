
class Graph:
    def __init__(self, size):
        self.adjList = [[] for _ in range(size)]
        
    def addEdge(self, u, v, w):
        self.adjList[u].append((v, w))
        self.adjList[v].append((u, w))
        
    def dijkstra(self, src):
        dist = [float('inf')] * len(self.adjList)
        dist[src] = 0
        
        pq = [(0, src)]
        while pq:
            currDist, currNode = heappop(pq)
            if currDist > dist[currNode]:
                continue
            
            for neighbor, weight in self.adjList[currNode]:
                if currDist | weight < dist[neighbor]:
                    dist[neighbor] = currDist | weight
                    heappush(pq, (dist[neighbor], neighbor))
        
        return dist
        
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)
    
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph.addEdge(a - 1, b - 1, w)
        
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        print(graph.dijkstra(s - 1)[t - 1])

