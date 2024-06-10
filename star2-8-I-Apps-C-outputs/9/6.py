
n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, w = map(int, input().split())
  edges[a].append([b, w])
  edges[b].append([a, w])
q = int(input())
costs = [0] * (q+1)
for i in range(1, q+1):
  s, t = map(int, input().split())
  costs[i] = costs[i-1]
print(*costs[1:], sep="\n")

