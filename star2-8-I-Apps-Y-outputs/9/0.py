
def solve():
  n, m = map(int, input().split())
  grid = [list(input()) for _ in range(n)]
  changed = True
  while changed:
    changed = False
    new_grid = [[c for c in row] for row in grid]
    for i in range(n):
      for j in range(m):
        if grid[i][j] == "V":
          if i > 0 and grid[i-1][j] == ".":
            new_grid[i-1][j] = "V"
            changed = True
          if i > 0 and j > 0 and grid[i-1][j-1] == ".":
            new_grid[i-1][j-1] = "V"
            changed = True
          if i > 0 and j < m-1 and grid[i-1][j+1] == ".":
            new_grid[i-1][j+1] = "V"
            changed = True
    grid = new_grid
  for row in grid:
    print("".join(row))

solve()

