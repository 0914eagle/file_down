
# Author : 
# Date   : 10 March, 2020


from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)


def create_graph(n, lis):
    graph = defaultdict(list)
    for i in range(n):
        for j in lis[i]:
            graph[i+1].append(j)

    return graph


def dfs(graph, src, visited, path):
    visited[src] = True
    for node in graph[src]:
        if visited[node]:
            continue
        path.append(node)
        visited[node] = True
        dfs(graph, node, visited, path)


if __name__ == "__main__":
    n = int(input())
    lis = []

    for _ in range(n):
        lis.append([int(x) for x in input().split()[1:]])

    graph = create_graph(n, lis)
    visited = [False]*(n+1)
    path = []

    dfs(graph, 1, visited, path)
    for node in path:
        for x in lis[node-1]:
            if x in path:
                print(node, x)
