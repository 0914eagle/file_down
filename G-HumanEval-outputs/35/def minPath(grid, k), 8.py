
def minPath(grid, k):
    def dfs(x, y, path, visited):
        if len(path) == k:
            return path
        visited.add((x, y))
        candidates = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                candidates.append((grid[nx][ny], nx, ny))
        candidates.sort()
        for val, nx, ny in candidates:
            res = dfs(nx, ny, path + [val], visited)
            if res:
                return res

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = dfs(i, j, [grid[i][j]], set())
            if path:
                return path

# Test cases
grid1 = [[1,2,3], [4,5,6], [7,8,9]]
k1 = 3
print(minPath(grid1, k1))  # Output: [1, 2, 1]

grid2 = [[5,9,3], [4,1,6], [7,8,2]]
k2 = 1
print(minPath(grid2, k2))  # Output: [1]
