
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

def count_adjacent_bombs(grid, row, col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '#':
            count += 1
    return count

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            grid[i][j] = str(count_adjacent_bombs(grid, i, j))

for row in grid:
    print(''.join(row))
