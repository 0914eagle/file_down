
from collections import defaultdict
def solve(n,m,roads):
  g = defaultdict(lambda:defaultdict(int))
  for u,v in roads:
    g[u][v] = 1
  indeg = defaultdict(int)
  outdeg = defaultdict(int)
  for u,v in g.items():
    outdeg[u] = len(v)
    for n in v.keys():
      indeg[n] += 1
  can = 0
  for i in range(1,n+1):
    if indeg[i] == outdeg[i]:
      can += 1
  print(can)
  return can

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n,m = map(int,input().split())
    roads = []
    for _ in range(m):
      u,v = map(int,input().split())
      roads.append([u,v])
    solve(n,m,roads)

