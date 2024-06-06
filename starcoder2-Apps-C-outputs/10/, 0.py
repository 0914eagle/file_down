
# 最小生成树
import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())

# 邻接表
graph = [[] for _ in range(n)]

# 邻接矩阵
matrix = [[0] * n for _ in range(n)]

for i in range(n - 1):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n - i - 1):
        matrix[i][i + j + 1] = matrix[i + j + 1][i] = line[j]
        heappush(graph[i], (line[j], i + j + 1))
        heappush(graph[i + j + 1], (line[j], i))

# 并查集
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y

# 最小生成树
mst = 0
for i in range(n):
    while graph[i]:
        weight, j = heappop(graph[i])
        if find(i) != find(j):
            mst += weight
            union(i, j)
            break

print(mst)
