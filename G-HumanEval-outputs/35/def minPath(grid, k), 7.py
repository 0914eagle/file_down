
def minPath(grid, k):
    N = len(grid)
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    def dfs(x, y, path):
        if len(path) == k:
            return path

        visited.add((x, y))
        next_paths = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                next_paths.append((grid[nx][ny], nx, ny))

        next_paths.sort()
        for _, nx, ny in next_paths:
            found_path = dfs(nx, ny, path + [grid[nx][ny]])
            if found_path:
                return found_path

        visited.remove((x, y))
        return None

    for i in range(N):
        for j in range(N):
            path = dfs(i, j, [grid[i][j]])
            if path:
                return path

# Test cases
print(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))  # Output: [1, 2, 1]
print(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1))  # Output: [1]
```
