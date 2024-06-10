
import sys
sys.setrecursionlimit(10**6)

n, d = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(1, n):
  x = int(input())
  tree[x].append(i)

def dfs(u, d):
  if len(tree[u]) == 0:
    return 1
  res = 0
  for v in tree[u]:
    res += dfs(v, d)
  return res

res = 0
for u in range(n):
  res = max(res, dfs(u, d))
print(res)

