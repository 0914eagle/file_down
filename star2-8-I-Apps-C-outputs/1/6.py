
from sys import stdin

def readline():
    return stdin.readline().strip()

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        
    def get_paths(self):
        paths = [[[] for _ in range(self.vertices)] for _ in range(self.vertices)]
        for u in range(self.vertices):
            for v in range(self.vertices):
                if self.graph[u][v] == 1:
                    paths[u][v] = [[u, v]]
        return paths
        
    def get_deliveries(self):
        paths = self.get_paths()
        deliveries = [[] for _ in range(self.vertices)]
        for u in range(self.vertices):
            for v in range(self.vertices):
                for path in paths[u][v]:
                    deliveries[u].append(path)
        return deliveries
        
    def get_max_producers(self):
        deliveries = self.get_deliveries()
        max_producers = 0
        for u in range(self.vertices):
            collisions = 0
            for v in range(self.vertices):
                if u != v and len(deliveries[u]) > 0 and len(deliveries[v]) > 0:
                    for path_u in deliveries[u]:
                        for path_v in deliveries[v]:
                            if path_u == path_v:
                                collisions += 1
            if collisions == 0:
                max_producers += 1
        
        return max_producers
    
n, k, m = map(int, readline().split())
graph = Graph(n)
for _ in range(m):
    u, v = map(int, readline().split())
    graph.add_edge(u - 1, v - 1)
    
print(graph.get_max_producers())

