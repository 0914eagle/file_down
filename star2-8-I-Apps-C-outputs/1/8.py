
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]
    
    def add_edge(self, u, v):
        self.graph[u][v] = 1
    
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        
        for i in range(self.V):
            if self.graph[v][i] == 1 and visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        
        stack.insert(0, v)
    
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        
        return stack
    
    def is_dag(self):
        stack = self.topological_sort()
        
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == 1:
                    if stack.index(i) > stack.index(j):
                        return False
        
        return True

def main():
    N, K, M = map(int, input().split())
    
    graph = Graph(N)
    
    for i in range(M):
        u, v = map(int, input().split())
        graph.add_edge(u - 1, v - 1)
    
    print(K if graph.is_dag() else K - 1)

if __name__ == '__main__':
    main()

