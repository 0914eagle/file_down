
import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
  n, m, alpha = map(int, input().split())
  adj_list = defaultdict(list)
  for _ in range(m):
    u, v, c = map(int, input().split())
    adj_list[u].append((v, c))
    adj_list[v].append((u, c))

  s = 1
  dist = defaultdict(int)
  parent = defaultdict(int)
  q = [s]
  while q:
    u = q.pop(0)
    for v, c in adj_list[u]:
      if v not in dist:
        dist[v] = dist[u] + c
        parent[v] = u
        q.append(v)

  max_candy = 0
  current = n
  while current != s:
    max_candy = max(max_candy, dist[current])
    current = parent[current]
  print(max_candy ** 2 + alpha * (m - 1))

if __name__ == '__main__':
  main()

