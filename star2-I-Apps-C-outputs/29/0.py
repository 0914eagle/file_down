
from math import sqrt

def dist(x1, y1, x2, y2):
  return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def is_in_sight(beacon1, beacon2, mountains):
  for mountain in mountains:
    if dist(beacon1[0], beacon1[1], mountain[0], mountain[1]) + dist(beacon2[0], beacon2[1], mountain[0], mountain[1]) <= mountain[2]:
      return False
  return True

def solve(beacons, mountains):
  n = len(beacons)
  graph = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(i+1, n):
      if is_in_sight(beacons[i], beacons[j], mountains):
        graph[i][j] = 1
        graph[j][i] = 1
  visited = [False for _ in range(n)]
  queue = [0]
  visited[0] = True
  while queue:
    curr = queue.pop(0)
    for i in range(n):
      if graph[curr][i] and not visited[i]:
        queue.append(i)
        visited[i] = True
  return n - visited.count(True)

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountains = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(beacons, mountains))

