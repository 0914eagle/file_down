
import sys
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.graph = [[] for i in range(vertices)]
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs_rec(self, s, visited, color):
        visited[s] = True
        
        for i in self.graph[s]:
            if not visited[i]:
                if color[i] == 0:
                    color[i] = -color[s]
                elif color[i] == color[s]:
                    return False
                if not self.bfs_rec(i, visited, color):
                    return False
        
        return True
    
    def is_bipartite(self):
        color = [0] * len(self.graph)
        visited = [False] * len(self.graph)
        
        for i in range(len(self.graph)):
            if not visited[i]:
                if color[i] == 0:
                    color[i] = 1
                if not self.bfs_rec(i, visited, color):
                    return False
        
        return True

def main():
    n = int(sys.stdin.readline())
    colors = [int(x) for x in sys.stdin.readline().split()]
    graph = Graph(n)
    
    for i in range(n - 1):
        v, u = [int(x) for x in sys.stdin.readline().split()]
        graph.add_edge(v - 1, u - 1)
    
    if graph.is_bipartite():
        print(n - 1)
    else:
        print(0)

if __name__ == "__main__":
    main()

