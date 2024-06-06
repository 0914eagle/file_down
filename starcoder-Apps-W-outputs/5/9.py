
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        visited = [False] * (max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

n, m = map(int, input().split())

g = Graph()
for i in range(m):
    u, v = map(int, input().split())
    g.addEdge(u, v)

if 1 in g.graph:
    g.BFS(1)
else:
    print('Connected')
