
import math

def dist(x1, y1, x2, y2):
  return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def is_in_range(x1, y1, x2, y2, r):
  return dist(x1, y1, x2, y2) <= r

def is_visible(x1, y1, x2, y2, mountains):
  for x, y, r in mountains:
    if is_in_range(x1, y1, x, y, r) or is_in_range(x2, y2, x, y, r):
      return False
  return True

def solve(beacons, mountains):
  n = len(beacons)
  graph = [[False] * n for _ in range(n)]
  for i in range(n):
    for j in range(i + 1, n):
      x1, y1 = beacons[i]
      x2, y2 = beacons[j]
      if is_visible(x1, y1, x2, y2, mountains):
        graph[i][j] = graph[j][i] = True
  visited = [False] * n
  queue = [0]
  visited[0] = True
  while queue:
    curr = queue.pop(0)
    for i in range(n):
      if graph[curr][i] and not visited[i]:
        visited[i] = True
        queue.append(i)
  return sum(not v for v in visited)

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountains = [tuple(map(int, input().split())) for _ in range(m)]

print(solve(beacons, mountains))

