
import sys

def BFS(s, t):
    q = [s]
    visited = [False] * V
    predecessor = [-1] * V
    while q:
        u = q.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                predecessor[v] = u
    path = [t]
    while predecessor[t] != -1:
        path.append(predecessor[t])
        t = predecessor[t]
    return path

def DFS(u, t, path, paths):
    if u == t:
        paths.append(path)
    else:
        for v in graph[u]:
            if v not in path:
                DFS(v, t, path + [v], paths)

def main():
    global V, graph
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append(v)
    s, t = map(int, input().split())
    path = BFS(s, t)
    if s == t or not path:
        print(0)
        return
    paths = []
    DFS(s, t, [s], paths)
    print(len(paths))

main()

