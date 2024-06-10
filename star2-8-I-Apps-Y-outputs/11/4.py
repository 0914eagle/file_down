
from collections import defaultdict
def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])
def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else :
        parent[yroot] = xroot
        rank[xroot] += 1
def kruskalMST(graph):
    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(V):
        parent.append(node)
        rank.append(0)
    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    return result
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append([j, a[j]])
    mst = kruskalMST(graph)
    if len(mst) == n - 1:
        print("YES")
        for edge in mst:
            print(edge[0] + 1, edge[1] + 1)
    else:
        print("NO")

