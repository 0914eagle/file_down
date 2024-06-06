
# 知识点: DFS
import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append([])
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)
if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    g = Graph(N)
    for i in range(M):
        u, v = map(int, sys.stdin.readline().strip().split())
        u -= 1
        v -= 1
        g.addEdge(u, v)
    visited = [False] * N
    g.DFS(0, visited)
    ans = []
    for i in range(N):
        if not visited[i]:
            ans.append(i + 1)
    if len(ans) == 0:
        print("Connected")
    else:
        for x in ans:
            print(x)
