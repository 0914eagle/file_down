
import sys
sys.setrecursionlimit(10**7)
N = int(input())
arr = [0]*N
par = [0]*N
for i in range(N):
  arr[i], par[i] = map(int, input().split())

def dfs(v, p):
  tmp = []
  for i in range(N):
    if par[i] == v:
      tmp.append(dfs(i, v))
  if tmp == []:
    return arr[v]
  else:
    return arr[v] + max(tmp)

print(dfs(0, 0))
