
def minPath(grid, k):
    def dfs(x, y, path):
        if len(path) == k:
            return path
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                visited.add((nx, ny))
                result = dfs(nx, ny, path + [grid[nx][ny]])
                if result:
                    return result
                visited.remove((nx, ny))
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            visited.add((i, j))
            result = dfs(i, j, [grid[i][j]])
            if result:
                return result

# Test cases
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3))  # Output: [1, 2, 1]
print(minPath([[5,9,3], [4,1,6], [7,8,2]], 1))  # Output: [1]
```
