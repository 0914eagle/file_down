
def solve_tomb_puzzle(n, m, floorplan):
    def is_valid_cell(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate_gargoyle(grid, x, y):
        if grid[x][y] == 'V':
            grid[x][y] = 'H'
        else:
            grid[x][y] = 'V'

    def dfs(x, y, direction):
        if not is_valid_cell(x, y) or visited[x][y]:
            return

        visited[x][y] = True

        if grid[x][y] in ['/', '\\', '#']:
            return

        if grid[x][y] == 'H' and direction in ['up', 'down']:
            rotate_gargoyle(grid, x, y)
            nonlocal rotations
            rotations += 1

        if grid[x][y] == 'V' and direction in ['left', 'right']:
            rotate_gargoyle(grid, x, y)
            rotations += 1

        if direction == 'up':
            dfs(x - 1, y, 'up')
        elif direction == 'down':
            dfs(x + 1, y, 'down')
        elif direction == 'left':
            dfs(x, y - 1, 'left')
        elif direction == 'right':
            dfs(x, y + 1, 'right')

    grid = [list(row) for row in floorplan]
    visited = [[False for _ in range(m)] for _ in range(n)]
    rotations = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] in ['V', 'H']:
                dfs(i, j, 'up')
                if not visited[i][j]:
                    return -1

    return rotations

# Input
n, m = map(int, input().split())
floorplan = [input().strip() for _ in range(n)]

# Output
print(solve_tomb_puzzle(n, m, floorplan))
```
