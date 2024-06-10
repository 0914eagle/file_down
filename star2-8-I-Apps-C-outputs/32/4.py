
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        
    def BFS(self, s):
        dist = [float("inf")] * self.V
        dist[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, w in self.graph[u]:
                if dist[v] == float("inf"):
                    dist[v] = dist[u] + w
                    queue.append(v)
        return dist

N, R = map(int, input().split())
graph = Graph(N)
for _ in range(R):
    a, b, c = map(int, input().split())
    graph.addEdge(a - 1, b - 1, c)
    graph.addEdge(b - 1, a - 1, c)
F = int(input())
for _ in range(F):
    a, b, c = map(int, input().split())
    graph.addEdge(a - 1, b - 1, c)
    graph.addEdge(b - 1, a - 1, c)
    
dist = graph.BFS(0)
print(dist[0])

