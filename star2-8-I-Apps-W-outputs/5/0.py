
[CODE]
from itertools import product

def find_way(maze, n, m, k):
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  directions = ["R", "L", "D", "U"]
  q = [(0, 0)]
  visited = set()
  while q:
    x, y = q.pop(0)
    if (x, y) not in visited:
      visited.add((x, y))
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "*" and (nx, ny) not in visited:
          q.append((nx, ny))
  if (n - 1, m - 1) not in visited:
    return "IMPOSSIBLE"
  for way in product(directions, repeat=k):
    x, y = 0, 0
    visited = set()
    for i in range(k):
      nx, ny = x + dx[directions.index(way[i])], y + dy[directions.index(way[i])]
      if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "*" and (nx, ny) not in visited:
        visited.add((nx, ny))
        x, y = nx, ny
      else:
        break
    if x == n - 1 and y == m - 1 and len(visited) == k:
      return "".join(way)
  return "IMPOSSIBLE"
[/CODE]

