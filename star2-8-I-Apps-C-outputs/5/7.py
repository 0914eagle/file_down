
import sys
input = sys.stdin.readline

def dfs(u):
  global marked
  for v in graph[u]:
    if dist[v] == -1:
      dist[v] = dist[u] + 1
      dfs(v)
  marked[u] = 1

N, D = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(1, N):
  x = int(input())
  graph[x].append(i)
  graph[i].append(x)
marked = [0] * N
marked[0] = 1
dist = [-1] * N
dist[0] = 0
dfs(0)
count = sum(marked)
print(count)

