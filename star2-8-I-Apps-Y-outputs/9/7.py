
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

def is_valid_pos(pos):
  r, c = pos
  return 0 <= r < N and 0 <= c < M

def check_water(pos):
  r, c = pos
  if grid[r][c] != ".":
    return
  for dr, dc in [(0, 1), (0, -1)]:
    if is_valid_pos((r + dr, c + dc)) and grid[r + dr][c + dc] == "V":
      grid[r] = grid[r][:c] + "V" + grid[r][c + 1:]
      break
  if grid[r][c] != "V":
    return
  for dr, dc in [(-1, 0), (0, 1), (0, -1)]:
    if is_valid_pos((r + dr, c + dc)) and grid[r + dr][c + dc] == ".":
      grid[r + dr] = grid[r + dr][:c + dc] + "V" + grid[r + dr][c + dc + 1:]

for r in range(N):
  for c in range(M):
    check_water((r, c))

for row in grid:
  print(row)

