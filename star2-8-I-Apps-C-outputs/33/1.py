
import sys
import math

def dfs(node):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            dfs(n)

n = int(sys.stdin.readline())
l = int(sys.stdin.readline())
path = list(map(int, sys.stdin.readline().split()))
graph = [[] for i in range(n)]
for i in range(n):
    n_i, *neighbours = map(int, sys.stdin.readline().split())
    graph[i] = neighbours
visited = [False] * n
dfs(path[0])
if not all(visited):
    print(0)
    exit()
visited = [False] * n
dfs(path[-1])
if not all(visited):
    print(0)
    exit()
total_ways = math.factorial(l)
unique_rooms = len(set(path))
ways_to_traverse = math.factorial(unique_rooms)
prob = ways_to_traverse / total_ways
print(prob)

