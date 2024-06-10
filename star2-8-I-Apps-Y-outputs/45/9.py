
from collections import deque

def dfs(u, p=-1):
  global red, blue
  for v in adj[u]:
    if v == p:
      continue
    dfs(v, u)
    red[u] += red[v]
    blue[u] += blue[v]

def dfs2(u, p=-1):
  global cnt
  for v in adj[u]:
    if v == p:
      continue
    cnt += (red[v] * (n - red[v]) + blue[v] * (n - blue[v]))
    dfs2(v, u)

n = int(input())
a = [int(i) for i in input().split()]
adj = [[] for _ in range(n)]
for _ in range(n-1):
  u, v = [int(i)-1 for i in input().split()]
  adj[u].append(v)
  adj[v].append(u)

red = [0] * n
blue = [0] * n
for i in range(n):
  if a[i] == 1:
    red[i] = 1
  elif a[i] == 2:
    blue[i] = 1

dfs(0)
cnt = 0
dfs2(0)
print(cnt)

