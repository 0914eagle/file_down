
def solve_grid(A, B):
    def get_next_cell(grid, visited, i, j):
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y]:
                return x, y
        return None

    def dfs(grid, visited, i, j, color):
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            visited[x][y] = True
            grid[x][y] = color
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '.' and not visited[nx][ny]:
                    stack.append((nx, ny))

    h, w = A + 1, B + 1
    grid = [['.' for _ in range(w)] for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                dfs(grid, visited, i, j, '.' if i < A else '#')

    print(f"{h} {w}")
    for row in grid:
        print(''.join(row))

# Read input
A, B = map(int, input().split())

# Call the function to solve the grid
solve_grid(A, B)
```
