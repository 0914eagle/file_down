
from collections import deque

def bfs(maze, start, fire):
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  maze[start[0]][start[1]] = 'J'
  queue = deque()
  queue.append(start)
  visited = set()
  visited.add(start)
  minutes = 0
  while queue:
    size = len(queue)
    for _ in range(size):
      curr = queue.popleft()
      for d in directions:
        neighbor = (curr[0] + d[0], curr[1] + d[1])
        if maze[neighbor[0]][neighbor[1]] == '.':
          maze[neighbor[0]][neighbor[1]] = 'J'
          queue.append(neighbor)
          visited.add(neighbor)
      if curr in fire:
        fire.remove(curr)
    if len(fire) == 0:
      return minutes
    minutes += 1
  return "IMPOSSIBLE"

def escape(maze):
  R = len(maze)
  C = len(maze[0])
  fire = set()
  start = None
  for i in range(R):
    for j in range(C):
      if maze[i][j] == 'F':
        fire.add((i, j))
      if maze[i][j] == 'J':
        start = (i, j)
  return bfs(maze, start, fire)

if __name__ == "__main__":
  R, C = map(int, input().split())
  maze = []
  for _ in range(R):
    row = list(input())
    maze.append(row)
  result = escape(maze)
  print(result)

