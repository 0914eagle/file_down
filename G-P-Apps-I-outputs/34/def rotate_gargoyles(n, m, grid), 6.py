
def rotate_gargoyles(n, m, grid):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate(gargoyle):
        if gargoyle == 'V':
            return 'H'
        elif gargoyle == 'H':
            return 'V'
        else:
            return gargoyle

    def check_path(x, y, dx, dy):
        while is_valid(x, y):
            if grid[x][y] == '#':
                return False
            if grid[x][y] != '.':
                return True
            x += dx
            y += dy
        return False

    def check_gargoyle(x, y):
        if grid[x][y] == 'V':
            if not check_path(x - 1, y, -1, 0) and not check_path(x + 1, y, 1, 0):
                return False
        elif grid[x][y] == 'H':
            if not check_path(x, y - 1, 0, -1) and not check_path(x, y + 1, 0, 1):
                return False
        return True

    rotations = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'V' or grid[i][j] == 'H':
                if not check_gargoyle(i, j):
                    grid[i][j] = rotate(grid[i][j])
                    rotations += 1
                    if not check_gargoyle(i, j):
                        return -1
    
    return rotations

# Input
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

# Output
result = rotate_gargoyles(n, m, grid)
print(result)
```
