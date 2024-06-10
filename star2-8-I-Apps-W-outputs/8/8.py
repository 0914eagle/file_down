
import sys

def is_triplet(grid, x, y, dx, dy):
  if 0 <= x + dx * 2 < N and 0 <= y + dy * 2 < N:
    if grid[x][y] != '.' and grid[x + dx][y + dy] != '.' and grid[x + dx * 2][y + dy * 2] != '.':
      return True
  return False

N = int(sys.stdin.readline())
grid = []
for _ in range(N):
  grid.append(list(sys.stdin.readline().strip()))

count = 0
for x in range(N):
  for y in range(N):
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        if dx == 0 and dy == 0:
          continue
        if is_triplet(grid, x, y, dx, dy):
          count += 1

print(count)

