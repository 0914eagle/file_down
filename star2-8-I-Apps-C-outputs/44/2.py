
def solve(h, w, grid):
  for i in range(h):
    grid[i] = list(grid[i])

  def dfs(x, y):
    if grid[x][y] == '+':
      grid[x][y] = ' '
      for dx in range(-1, 2):
        for dy in range(-1, 2):
          nx = x + dx
          ny = y + dy
          if 0 <= nx < h and 0 <= ny < w:
            dfs(nx, ny)

  for i in range(h):
    for j in range(w):
      if grid[i][j] == '+':
        dfs(i, j)

  for i in range(h):
    grid[i] = ''.join(grid[i])
  return grid

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
grid = solve(h, w, grid)
for line in grid:
  print(line)

